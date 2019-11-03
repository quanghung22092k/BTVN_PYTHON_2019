# Ban đầu tưởng hiêu cầu của đề là mã hóa
# s = input()
# x = ""
# while s != "":
# 	i = (len(s) - 1) // 2
# 	x += s[i]
# 	s = s[:i] + s[i+1:]
# print(x)

arr = input()
print(arr[-2::-2]+arr[::2])