import sys
import math


###### First attempt, bad look at time complexity, have a for loop in a for loop would be cheaper to just brute force it
def is_prime(x):
	
	#print("floor = ", math.floor(x**.5))
	for i in range(2, math.floor(x**.5)+1):
		#print(i)
		if x % i == 0:
			# print(x, "is not prime")
			return 0
	#print(x, "is prime")
	return x





# look at all numbers in the range from 998,001

# is palindrome
def num_len(num):
	return math.floor(math.log10(num)) + 1

def ispal(num):
	lngth = num_len(num)
	palin = 0
	temp = 0

	for i in range(1, lngth+1):
		#print("i = ", i)
		temp = int(num / (10**(lngth-i))) #get rid of everhthing behind
		#print("first", temp)
		temp = temp % 10 #get rid of everything in front
		#print("second", temp) 
		temp = temp * 10**(i-1)
		#print("final temp", temp)
		palin += temp
		#print(palin)
		#print()

	if palin == num:
		return True
		
	else :
		return False

# now need to figure out is a number is a factor of two three digit numbers
# can' think of anthing besides a nested for loop


# go through all possible combination of 3 digit numbers and then see if 
# they are a palindrome, if they are see if largest so far
def largest():
	maxpal = 0
	for a in range(999, 99, -1):
		for b in range(a, 99, -1):
			temp = a*b
			if ispal(temp):
				if temp > maxpal:
					maxpal = temp
	print(maxpal)
	return maxpal


largest()
# Ans = 906609



		


# print(ispal(101))

# print(ispal(122))

# print(ispal(10001))

# print(ispal(110000))


		



#2334
#2334 / 10^len-i * 10 ^ i - 1


#(2334 / 10 ^ len - i) % 10 * 10 ^ i - 1


	
		










#print(is_prime())
			

