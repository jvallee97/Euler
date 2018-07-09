import sys

def euler_1(max):
	ret = 0
	for i in range(1, max):
		if i % 3 == 0 or i % 5 == 0:
			ret = ret + i
	print(ret)
			


euler_1(10)

euler_1(1000)




# euler_1(7)
# #3 +5 + 6 = 14

# euler_1(16)
# 3 + 5 + 6 + 9 + 10 + 12 + 15 = 60

		