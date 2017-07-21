'''
ESWL - Easy and Simple Web Library
With it you can create web apps, multiplayer games and more very fast
For tutorials see: ttxsoft.github.io/ESWL/tutorials.html
'''
import socket
import pickle
def send_to(ip,port,val):
	proto = socket.getprotobyname('tcp')
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto)
	s.bind((ip,port))
	s.listen(1)
	while True:
		conn,addr = s.accept()
		if conn:
			conn.send(pickle.dumps(val))
			break
def recv_from(ip,port):
	proto = socket.getprotobyname('tcp')
	c = socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto)
	c.connect((ip,port))
	return pickle.loads(c.recv(1024))
