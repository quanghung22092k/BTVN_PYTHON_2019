
num = 1221
r = 0
sum = 0
temp = num

while num!=0 :
    r=num%10
    sum = sum*10+r
    num = num/10
if temp==sum:
    print(0)
else:
    print(1)

