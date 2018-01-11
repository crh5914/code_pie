class Calculator:
    def __init__(self,exp):
        exp = exp.strip()
        self.polish_exp = self.parse(exp)
    def parse(self,exp):
        s0 = []
        j = 0
        for i in range(len(exp)):
            if exp[i] == ' ':
                if j < i:
                    s0.append(Operand(exp[j:i]))
                j = i + 1 
            elif exp[i] in ['*','/','+','-']:
                if j < i:
                    s0.append(Operand(exp[j:i]))
                j = i
                s0.append(Operator(exp[j:i+1]))
                j += 1
            elif exp[i] in ['{','}','[',']','(',')']:
                if j < i:
                    s0.append(Operand(exp[j:i]))
                j = i
                s0.append(Delimitor(exp[j:i+1]))
                j += 1
        if j <= len(exp)-1:
            if exp[-1] in ['{','}','[',']','(',')']:
                s0.append(Delimitor(exp[-1]))
            else:
                s0.append(Operand(exp[j:]))
        s1 = []
        s2 = []
        for tk in s0:
            if type(tk) == Operator:
                if len(s2)>0:
                    if type(s2[-1])==Operator and s2[-1].priorto(tk):
                        s1.append(s2.pop())
                        s2.append(tk)
                    else:
                        s2.append(tk)
                else:
                    s2.append(tk)
            elif type(tk) == Operand:
                s1.append(tk)
            elif type(tk) == Delimitor:
                if tk.value in ['}',']',')']:
                    while True:
                        if len(s2)==0:
                            raise ValueError('Invalid experssion')
                        t = s2.pop()
                        if type(t)==Delimitor:
                            if tk.match(t):
                                break
                            else:
                                raise ValueError('Invalid experssion') 
                        else:
                            s1.append(t)  
                else:
                    s2.append(tk)            
        while len(s2):
            s1.append(s2.pop())
        return s1
    def eval(self):
        operands = []
        for op in self.polish_exp:
            if type(op) == Operand:
                operands.append(op)
            elif type(op) == Operator:
                op1 = operands.pop()
                op2 = operands.pop()
                operands.append(op.opon(op2, op1))
        print(operands)
        if len(operands) == 1:
            return operands.pop().value
        else:
            raise ValueError('Invalid experssion.')
class Operand:
    def __init__(self,s):
        self.value = self.parse(str(s).strip())
    def parse(self,str):
        if '.' in str:
            return self.__atod(str)
        else:
            return self.__atoi(str)
    def __atoi(self,str):
        i=res=0
        flag = 1
        if str[i]=='-':
            flag = -1
            i += 1
        elif str[i] == '+':
            i += 1
        end = len(str) - i
        while i < end:
            if str[i]>'9' or str[i]<'0':
                raise ValueError('Invalid integer')
            d = ord(str[i])-ord('0')
            res = res*10 + d
            i += 1
        return flag*res          
    def __atod(self,str):
        i = q= r=0
        flag = 1
        if str[i]=='-':
            flag = -1
            i += 1
        elif str[i] == '+':
            i += 1
        end = len(str) - i 
        while i < end:
            if str[i]>'9' or str[i]<'0':
                if str[i] == '.':
                    break;
                else:
                    raise ValueError('Invalid integer')
            d = ord(str[i])-ord('0')
            q = q*10 + d
            i += 1
        j = len(str)-1 
        while j>i:
            if str[j]>'9' or str[j]<'0':
                raise ValueError('Invalid integer')
            d = ord(str[j])-ord('0')
            r = (r + d)/10
            j -= 1
        return flag*(q+r)
    def __repr__(self):
        return str(self.value)
class Operator:
    ops = ['*','-','/','+']
    def __init__(self,str):
        self.op =str.strip()if str.strip() in self.ops else None
    def priorto(self,op):
        if self.op in ['*','/'] and op.op in ['+','-']:
            return True
        return False
    def opon(self,op1,op2):
        if self.op == '*':
            return Operand(op1.value*op2.value)
        elif self.op == '/':
            return Operand(op1.value/op2.value)
        elif self.op == '+':
            return Operand(op1.value+op2.value)
        else:
            return Operand(op1.value-op2.value)
    def __repr__(self):
        return self.op
class Delimitor:
    def __init__(self,s):
        s = s.strip()
        if s in ['{','}','(',')','[',']']:
            self.value = s
    def match(self,d2):
        if (self.value == ')' and d2.value == '(') or(self.value == ']' and d2.value == '[')or(self.value == '}' and d2.value == '{') :
            return True
        return False
    def __repr__(self):
        return self.value
if __name__ == '__main__':
    exp = ' { [ ( 1 + 3 * 2.0 ) + 3 ] * 7} / (3.0/34+8*6) '
    cal = Calculator(exp)
    print(cal.eval())