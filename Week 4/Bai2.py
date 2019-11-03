a1, a2, a3, a4 = map(int, input().split())
b1, b2, b3, b4 = map(int, input().split())
Sa = (a3 - a1)*(a4 - a2)
Sb = (b3 - b1)*(b4 - b2)
xc = min(a3, b3) - max(a1, b1)
yc = min(a4, b4) - max(a2, b2)
if(xc > 0 and yc > 0):
	Sc = (min(a4, b4) - max(a2, b2))*(min(a3, b3) - max(a1, b1))
	if((a1 < b1) and (a2 < b2) and (a3 > b3) and (a4 > b4)):
		print(Sa - Sb)
	elif((b1 < a1) and (b2 < a2) and (b3 > a3) and (b4 > a4)):
		print(Sb - Sa)
	else:
		print(Sa + Sb - 2*Sc)
else:
	print(Sa + Sb)