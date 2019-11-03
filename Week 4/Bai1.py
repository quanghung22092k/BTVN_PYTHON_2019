s = input()
x = ""
while s != "":
	i = (len(s) - 1) // 2
	x += s[i]
	s = s[:i] + s[i+1:]
print(x)