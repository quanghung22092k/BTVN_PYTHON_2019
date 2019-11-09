def nhapMang(x):
	x = list(map(int,input().split(' ')))
	return x

def phanTuChung(a, b):
	a.sort()
	b.sort()
	for i in range (0, len(a)):
		for j in range (0, len(b)):
			if a[i] == a[i-1]:
				break
			if a[i] == b[j]:
				print(a[i], end = " ")
				break

a = []
b = []
print("Nhap mang A: ", end = "")
a = nhapMang(a)
print("Nhap mang B: ", end = "")
b = nhapMang(b)
print("Phan tu chung cua A va B:", end = "")
phanTuChung(a, b)