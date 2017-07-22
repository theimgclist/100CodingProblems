# Created by Avinash on 21st July, 2017
import sys
def nth_fibonacci_number_memoization(n, memo):
	if memo[n] == -1:
		if n <= 1:
			memo[n] = n
		else:
			memo[n] = nth_fibonacci_number_memoization(n-1,memo) + nth_fibonacci_number_memoization(n-2,memo);
	return memo[n];

def nth_fibonacci_number_tabulation(n, memo):
	memo[0] = 0
	memo[1] = 1
	for i in range(2, n+1):
			memo[i] = memo[i-1] + memo[i-2]
	return memo[n]

def nth_fibonacci_number_iterative(n):
	if n == 0:
		return 0
	term1 = 0
	term2 = 1
	temp = 0
	for i in range(2, n+1):
		temp = term2
		term2 = term1 + term2
		term1 = temp	
	return term2 

def process():
	n = int(input("Enter the fibonacci term "))
	memo = [-1]*(n+1)
	#print("The %dth Fibonacci term is %d" %(n, nth_fibonacci_number_memoization(n-1,memo)))
	#print("The %dth Fibonacci term is %d" %(n, nth_fibonacci_number_tabulation(n-1,memo)))
	print("The %dth Fibonacci term is %d" %(n, nth_fibonacci_number_iterative(n-1)))
	

if __name__=="__main__":
	process()