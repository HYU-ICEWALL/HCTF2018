import socket
import urllib2

print "socket ready..."

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('54.180.60.212',3002)
sock.connect(server)

print "connected..."

recv_data = sock.recv(10000)
print recv_data

recv_data = sock.recv(10000)
print recv_data

first = open("shattered-1.pdf","rb").read()[:500]
second = open("shattered-2.pdf","rb").read()[:500]

sock.send(first + '\n')

print "first send!"

recv_data = sock.recv(10000)
print recv_data

sock.send(second + '\n')

recv_data = sock.recv(10000)
print recv_data

sock.close()


