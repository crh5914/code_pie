import socket
import threading
host = '127.0.0.1'
port = 5000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('[*] Server start..')
def handle_request(client):
	client.send("Nice to provide service for you.")
	res = client.recv(2048)
	print('[*] Recive message from user:{}'.format(res.decode('utf-8')))

while True:
	client,addr = server.accept()
	print('[*] A client connected.')
	handler = threading.Thread(target=handle_request,args=client)
	client.close()
	print('[*] Serve a client done.')
