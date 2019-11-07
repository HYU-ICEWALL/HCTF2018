import socket
import threading

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
				client.send("[+] Welcome to the CCC (Classical Cipher Challenge)\n")

				client.send("\n[+] Stage 1/3 - Caesar")
				client.send("\n[+] Cipher: Gl apwnrmepynfw, y Aycqyp agnfcp, yjqm ilmul yq Aycqyp'q agnfcp, rfc qfgdr agnfcp, Aycqyp'q ambc mp Aycqyp qfgdr, gq mlc md rfc qgknjcqr ylb kmqr ugbcjw ilmul clapwnrgml rcaflgoscq.")
				client.send("\n[+] Answer: ")
				C1_anwser = client.recv(1024).strip()

				if not "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques." in C1_anwser:
					client.close()
					return False

				client.send("\n[+] Stage 2/3 - Base??")
				client.send("\n[+] Cipher: IJQXGZJTGIQGS4ZAN5XGKIDPMYQHGZLWMVZGC3BAMJQXGZJAGMZCA5DSMFXHGZTFOIQGK3TDN5SGS3THOMXA====")
				client.send("\n[+] Answer: ")
				C2_anwser = client.recv(1024).strip()

				if not "Base32 is one of several base 32 transfer encodings." in C2_anwser:
					client.close()
					return False

				client.send("\n[+] Stage 3/3 - Null")
				client.send("\n[+] Cipher: kimchi diet & donerts game is gym anyware & anytime!")
				client.send("\n[+] Answer: ")
				C3_anwser = client.recv(1024).strip().lower()

				if not "kingsman" in C3_anwser:
					client.close()
					return False

				client.send("\n[+] Flag: " + "XSJV{jxuhu_4hu_c4do_s1qiiysqb_s1fxuhi_1d_jxu_m0hbt}".encode('base64').strip())
				client.close()
			except:
				client.close()
				return False

ThreadServer('0.0.0.0', 3001).listen()