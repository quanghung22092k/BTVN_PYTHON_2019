a1, a2, a3, a4 = map(int, input().split())
b1, b2, b3, b4 = map(int, input().split())
Sa = (a3 - a1)*(a4 - a2)
Sb = (b3 - b1)*(b4 - b2)
Sc = (min(a4, b4) - max(a2, b2))*(min(a3, b3) - max(a1, b1))
if(Sc < 0):
    print(Sa + Sb)
else:
    print(Sa + Sb - 2*Sc)