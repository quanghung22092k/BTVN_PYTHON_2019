def nhapMang(x):
	x = list(map(int,input().split(' ')))
	return x

def sum(a, b):
	c = []
	for i in range (0, min(len(a), len(b))):
		c.insert(i, a[i] + b[i])
	for i in range (min(len(a), len(b)), max(len(a), len(b))):
		if(len(a) > len(b)):
			c.insert(i, a[i])
		else:
			c.insert(i, b[i])
	return c
	
a = []
b = []
print("Nhap mang A: ", end = "")
a = nhapMang(a)
print("Nhap mang B: ", end = "")
b = nhapMang(b)
print("A + B =",sum(a,b))