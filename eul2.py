import sys

def fib(len):
	ret = 0
	prev = 1
	p_prev = 0
	nex = 0
	while prev + p_prev <= len:
		nex = prev + p_prev
		p_prev = prev
		prev = nex 
		if nex % 2 ==0:
			ret = nex + ret
	print(ret)
	

fib(4000000)
			

# cache = {}
# def fiba(n):
#      cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fiba(n-1) + fiba(n-2))
#      return cache[n]
# n = 0
# x = 0
# while fiba(x) <= 4000000:
#        if not fiba(x) % 2: n = n + fiba(x)
#        x=x+1
# print(n)
