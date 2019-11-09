def nhapTen(a, n):
	for i in range (0, n):
		a.append(str(input()))

def winer(a,n):
	a.sort()
	max = 0
	for i in range (0, n):
		if a[i] == a[i-1]:
			break
		if max < a.count(a[i]):
			max = a.count(a[i])
	print("Ket qua:")
	for i in range (0, n):
		if a[i] == a[i-1]:
			continue
		if a.count(a[i]) == max:
			print(a[i])

n = int(input())
a = []
nhapTen(a,n)
winer(a,n)