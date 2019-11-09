def chiaKeo():
	i = 0
	j = n-1
	while i <= k:
		suml += a[i]
		i += 1
	while j > k:
		sumr += a[j]
		j -= 1
	min = abs(suml - sumr)

n = int(input())
a = list(map(int,input().split(' ')))

k = (n-1)//2
	
if suml < sumr :
	k += 1
if suml > sumr :
	k -= 1
print()
