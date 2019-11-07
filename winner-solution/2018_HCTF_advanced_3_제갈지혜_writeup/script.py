with open("script", "rb") as f:
	s = f.read()
idx = 0
flag = []
while idx < len(s):
	if s[idx] == 0x3c:
		flag.append(s[idx+1])
	idx += 1
flag_string = ""
for c in flag:
	flag_string += chr(c)
