import sys

def euler_1(max):

	num = 3*5
	i = 0
	ret = 0

	# print("b4 while")
	while num < max:
		# print("i = ", i)
		num = 15 * (i + 1)
		if num >= max:
				break
		ret = num + ret
		i = i + 1

	# print("after")
	num = 3 
	i = 0


	while num < max:
		# print("after while3")
		# print("b4 num = ", num)
		# print("i = ", i)
		num = 3 * (i + 1)
		i = i + 1

		if num >= max:
			break 

		if num % 5 == 0:
			pass

		else:
			ret = num + ret


	num = 5 
	i = 0

	while num < max:
		num = 5 * (i + 1)
		if num >= max:
			# print("break")
			i = i + 1
			break
		if num % 3 == 0:
			i = i + 1

		else:
			ret = num + ret
			i = i + 1


	return ret



	# print("lsboth", ls_both)
	# print("ls3", ls3)
	# print("ls5", ls5)

	



print(euler_1(1000))

# euler_1(1000)


# euler_1(7)
# #3 +5 + 6 = 14

# euler_1(16)
# 3 + 5 + 6 + 9 + 10 + 12 + 15 = 60

		