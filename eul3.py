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





#returns largest prime factor of a x (assume x not prime)
def prime():
	cash = []
	x = int(input("x = ", ))
	for i in range(2, math.floor(x/2)+1):
		if x % i == 0:
			cash.insert(len(cash), x/i)
	for i in cash:
		if is_prime(i):
			return i
	return 0



#####DONE ATTEMPT ONE######


# Second Attempt, I will go through the factors up to the half way point 
#(given by square root) then construct remaining factors and see where I get
# a prime in that list

def factors(x):
	factors = []
	#print("floor = ", math.floor(x**.5))
	for i in range(2, math.floor(x**.5)+1):
		if x % i == 0: 
			factors.extend([i, x/i])

	return factors



def is_prime_1(x):	
	#print("floor = ", math.floor(x**.5))
	for i in range(2, math.floor(x**.5)+1):
		#print(i)
		if x % i == 0:
			# print(x, "is not prime")
			return 0
	#print(x, "is prime")
	return x

#damn I still get an embedded for loop if I try to do it this way
def largest_prime(x):
	facts = factors(x)


##### STOPPED ATTEMPT 2 #####

# attempt 3 
# will make a list of prime factors then select the last one

def prime_facts(x):
	p_factors = []
	temp = x
	#print("x = ", x)
	while(temp % 2 == 0): #will give us how mny times two appears
		#print("temp % 2 == 0")
		if temp == x:
			p_factors.insert(0, 2)
		temp = temp/2
	# know it must be odd
	for i in range(3, int(temp**.5 + 1), 2):
		#print("i = ", i ," temp = ", temp)
		#if temp % i == 0:
		while temp % i == 0:			
			temp = temp/i
			p_factors.insert(0, i)
	if temp > 2:
		p_factors.insert(0, temp) # if reaches guarenteed to be largest

	print(p_factors[0])	



prime_facts(600851475143)

			

		










#print(is_prime())
			

