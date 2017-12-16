# Created by Avinash on 16th Dec, 2017
import sys
def process() :
	data = input("Enter the data")
	n = len(data)
	isPal = [[False for i in range(n)]for j in range(n)]
	isPal = palCheck(data)
	minSplits = palPartition(data,isPal)
	print("The minimum number of cuts required for palindrome partitioning is %d"%minSplits)

def palCheck(data):
	n = len(data)
	isPal = [[False for i in range(n)]for j in range(n)]
	for i in range(n):
		isPal[i][i] = True
	for i in range(n-1):
		if data[i] == data[i+1] :
			isPal[i][i+1] = True
	for l in range(3,n+1):
		for i in range(0,n-l+1):
			j = i+l-1
			if data[i] == data[j] and isPal[i+1][j-1] :
				isPal[i][j] = True
	return isPal

def palPartition(data,isPal):
	n = len(data)
	splits = [0 for i in range(n)]
	for i in range(n):
		min = sys.maxsize
		if isPal[0][i] :
			splits[i] = 0
		else :
			for j in range(i):
				if isPal[j+1][i] and min > splits[j]+1 :
					min = splits[j] + 1
			splits[i] = min
	return splits[n-1]	
			

if __name__ == "__main__":
	process()
	