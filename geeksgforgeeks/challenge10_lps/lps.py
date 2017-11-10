# Created by Avinash on 10th Nov, 2017
import sys
def process():
	data = input("Enter the string : ")
	lps = lpsCache(data,0,len(data)-1)
	print("The length of longest palindromic sequence is %-5d" %lps)

def lpsrec(data,i,j):
	if i == j :
		return 1
	if data[i] == data[j] and i + 1 == j:
		return 2
	if data[i] == data[j] :
		return 2 + lpsrec(data, i + 1, j - 1)
	return max(lpsrec(data,i,j-1), lpsrec(data,i+1,j))	

def lpsCache(data,i,j):
	n = len(data);
	cache = [[ 0 for j in range(n)] for i in range(n)]
	for i in range(n):
		cache[i][i] = 1
	for sub in range(2,n+1):	
		for i in range(0,n-sub+1):
	 		j = i + sub - 1
	 		if data[i] == data[j] and sub == 2 :
	 			cache[i][j] = 2 
	 		elif data[i] == data[j] :
	 			cache[i][j] = 2 + cache[i+1][j-1]
	 		else :
	 			cache[i][j] = max(cache[i+1][j], cache[i][j-1])
	 	
	return cache[0][n-1]
					

if __name__=="__main__":
	process()
		
			