import md5
import socket
import threading

salt = "jeong.su"
flag = "HCTF{the_s4lt_i5_to0_sal7y_:(}"

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
				client.send("[+] Welcome to the SSS (Salt Signature System)\n")
				client.send("[+] md5(super_secret_salt+'test'): %s\n" % md5.new(salt + "test").hexdigest())
	
				client.send("\n[+] Input Your Message: ")
				Message = client.recv(1024).strip()

				client.send("\n[+] Input Your Signature: ")
				Signature = client.recv(1024).strip()

				if Signature == md5.new(salt + Message).hexdigest():
					if Message == "test":
						client.send("\n[-] Your signature is processed normally. But I want another Message.")
						client.close()
						return False
					else:
						client.send("\n[+] Flag: %s" % flag)
						client.close()
						return False
				else:
					client.send("\n[-] Unauthenticated message. Do you like Salt?")
					client.close()
					return False
			except:
				client.close()
				return False

ThreadServer('0.0.0.0', 3003).listen()