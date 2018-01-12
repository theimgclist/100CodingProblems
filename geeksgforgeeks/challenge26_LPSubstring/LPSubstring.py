"""
	Created by Avinash on 12th Jan 2017
"""
import sys
def process():
	data = input("Enter the string : ")
	lps = lpsCache(data)
	print("The length of longest palindromic substring is %-5d" %lps)

def lpsCache(data):
	n = len(data);
	cache = [[ 0 for j in range(n)] for i in range(n)]
	for i in range(n):
		cache[i][i] = 1 # each character in the string is a palindrome of length 1
	maxlen = 1	
	for sub in range(2,n+1): # sub represents the size of substring, we start with 2 and check until n	
		for i in range(0,n-sub+1): # for the current substring size, this gives the starting index 
	 		j = i + sub - 1   # this is the ending index for the current substring size
	 		if data[i] == data[j] and sub == 2 : # if both characters are same, we have a palindrome of length 2
	 			cache[i][j] = True
	 			maxlen = 2
	 			start = i
	 			
	 		elif data[i] == data[j] and cache[i+1][j-1] : # for a substring of length > 2, we check if its palindrome
	 			cache[i][j] = True
	 			maxlen = sub
	 			start = i
	printLPS(data,start,maxlen)	
	 		
	return maxlen

def printLPS(data,start,maxlen) :
	print(data[start:start+maxlen])
					

if __name__=="__main__":
	process()

	