# Created by Avinash on 4th August, 2017
def process():
	amount = int(input("Enter the amount : "))
	coins = int(input("Enter the number of denominations : "))
	denominations = [[0] for i in range(coins)]
	print("Enter the denominations : ")
	for i in range(coins) : 
		denominations[i] = int(input())
	coinChangeWays = coinChange(amount,coins,denominations)
	print("The total number of ways to make the change using coins is : %-5d" %coinChangeWays)

def coinChange(n, m, d) :
	cache = [[0] * (n + 1) for i in range(m)]
	for i in range(m) :
		cache[i][0] = 1
	for i in range(m) :
		for j in range(1,n + 1) :
			include_coin = cache[i][j - d[i]] if (j - d[i] >= 0) else 0
			exclude_coin = cache[i - 1][j] if i >= 1 else 0
			cache[i][j] = include_coin + exclude_coin
	return cache[m-1][n]

if __name__=="__main__":
	process()
		
	