import sha
import socket
import threading

flag = "HCTF{7he_thre4t_if_1_am_n0t_9iven_a_g1ft:)}"

class ThreadServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def listen(self):
		self.sock.listen(5)
		while True:
			client, addr = self.sock.accept()
			client.settimeout(30)
			threading.Thread(target=self.doClient, args=(client, addr)).start()

	def doClient(self, client, addr):
		while True:
			try:
				client.send("[+] Welcome to the ToT (Trick or Threat)\n")
				client.send("\n[+] Trick or Threat!\n")
	
				client.send("\n[+] Give me Chocolate: ")
				chocolate = client.recv(1024).strip()

				client.send("[+] Give me Candy: ")
				candy = client.recv(1024).strip()

				if chocolate == candy:
					client.send("\n[-] No, these two must be different.")
					client.close()
					return False
				elif sha.new(chocolate).hexdigest() == sha.new(candy).hexdigest():
					client.send("\n[+] Flag: %s" % flag)
					client.close()
					return False
				else:
					client.send("\n[-] Nice! but, these sha1 hash must be same.")
					client.close()
					return False
			except:
				client.close()
				return False

ThreadServer('0.0.0.0', 3002).listen()