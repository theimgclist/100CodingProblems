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
	
            
def process():
	n = int(input("Enter the fibonacci term "))
	memo = [-1]*(n+1)
	print("The %dth Fibonacci term is %d" %(n, nth_fibonacci_number_memoization(n-1,memo)))
	#print("The %dth Fibonacci term is %d" %(n, nth_fibonacci_number_tabulation(n-1,memo)))
	

if __name__=="__main__":
	process()
