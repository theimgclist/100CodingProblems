# Created by Avinash on 20th Sept, 2017
def process():
	k_w = int(input("Enter the weight of knapsack: "))
	n = int(input("Enter number of items : "))
	i_w = [ 0 for i in range(n+1)]
	i_v = [ 0 for j in range(n+1)]
	print("Enter the item weights")
	for i in range(n):
		i_w[i] = int(input())
	print("Enter the item values")	
	for i in range(n):
		i_v[i] = int(input())
	capacity = knapsack(k_w,n,i_w,i_v)
	print("The capacity of knapsack for given items is %-5d" %capacity)

def knapsack_recursion(k_w,n,i_w,i_v):
	if n == 0 or k_w == 0 :
		return 0
	if i_w[n-1] > k_w :
		return knapsack_recursion(k_w,n-1,i_w,i_v)
	else :
		return max(i_v[n-1] + knapsack_recursion(k_w - i_w[n-1],n-1,i_w,i_v),
		knapsack_recursion(k_w,n-1,i_w,i_v))

def knapsack(k_w,n,i_w,i_v):
	cache = [[ 0 for j in range(k_w + 1)] for i in range(n + 1)]
	for i in range(n+1):
		for j in range(k_w + 1):
			if i == 0 or j == 0:
				cache[i][j] = 0
			elif i_w[i - 1] <= j :
				cache[i][j] = max(i_v[i] + cache[i-1][k_w - i_w[i-1]],
				cache[i-1][j])
			else :
				cache[i][j] = cache[i-1][j]
	return cache[n][k_w]
			

if __name__ == "__main__":
	process()
	
	
	
	