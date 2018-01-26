import socket

host = '127.0.0.1'
port = 5000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

client.send("Hello server, I'm client.\n".encode('utf-8'))
res = client.recv(2048)
print('[*] Recive data from server:{}\n'.format(res))