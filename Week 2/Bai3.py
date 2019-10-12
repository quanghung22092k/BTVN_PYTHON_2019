print('--- CHUONG TRINH HIEN THI DAY SO CHINH PHUONG ---')
n = int(input('Nhap vao mot so nguyen: '))
for i in range (1,n):
	if int(i**(1/2))==i**(1/2):
		print(i, end =' ')