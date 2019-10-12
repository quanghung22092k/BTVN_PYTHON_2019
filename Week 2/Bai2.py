print('----- BAI 2 -----')
a = float(input('Nhap canh a cua tam giac: '))
b = float(input('Nhap canh b cua tam giac: '))
c = float(input('Nhap canh c cua tam giac: '))
max = a
if max < b:
	max = b
if max < c:
	max = c
print('Canh dai nhat cua tam giac: ',max)
cv = a+b+c
print('Chu vi tam: ',cv)
p = cv/2
s = (p*(p-a)*(p-b)*(p-c))**(1/2)
print('Dien tich tam giac: ',s)