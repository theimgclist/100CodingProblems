# Created by Avinash on 13th Nov, 2017
import sys
def process():
	n = int(input("Enter the length of the rod : "))
	price = [ 0 for i in range(n)]
	print("Enter the price of different lengths of rod : ")
	for i in range(n):
		price[i] = int(input())
	maxPrice = findMaxPriceDP(price,n)
	print("The maximum price that can be obtained is %-5d" %maxPrice)

def findMaxPrice(price,length):
	if length <= 0 :
		return 0
	maxPrice = -sys.maxsize
	for i in range(0,length):
		maxPrice = max(maxPrice, price[i] + findMaxPrice(price,length-i-1))
	return maxPrice

def findMaxPriceDP(price, length):
	cache = [0 for i in range(0,length+1)]
	maxPrice = -1
	for i in range(1,length+1):
		for j in range(0,i):
			maxPrice = max(maxPrice,price[j]+cache[i-j-1])
			cache[i] = maxPrice
	return cache[length]	

				

if __name__=="__main__":
	process()
		
			