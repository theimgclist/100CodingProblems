"""
	Created by Avinash on 9th Jan, 2017
"""
def findnth_ugly_number(n) :
	ugly_list = [0 for i in range(n)] # or [0] * n
	ugly_list[0] = 1 # since first number in the list of ugly numbers is 1
	i2 = i3 = i5 = 0 # We will be using the multiples of primes numbers 2,3,5 to solve this problem
	next_mul_2 = 2
	next_mul_3 = 3
	next_mul_5 = 5
	for i in range(1,n) :
		ugly_list[i] = min(next_mul_2, next_mul_3, next_mul_5)
		if(ugly_list[i] == next_mul_2) :
			i2 += 1
			next_mul_2 = ugly_list[i2] * 2
		if(ugly_list[i] == next_mul_3) :
			i3 += 1
			next_mul_3 = ugly_list[i3] * 3
		if(ugly_list[i] == next_mul_5) :
			i5 += 1
			next_mul_5 = ugly_list[i] * 5
	return ugly_list[-1]	
	 
if __name__ == "__main__" :
	n = int(input("Enter the n value "))
	nth_ugly_number = findnth_ugly_number(n)
	print("The %d"%n+"th ugly number is %d"%nth_ugly_number)	