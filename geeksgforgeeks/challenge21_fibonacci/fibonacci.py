"""
	Created by Avinash on 4th Jan, 2017
"""
def fibonacci(n) :
	fib = [0 for i in range(n)]
	fib[0] = 0
	fib[1] = 1
	for i in range(2,n):
		fib[i] = fib[i-1] + fib[i-2]
	print(fib[n-1])

if __name__ == "__main__":
	fibonacci(10)
	