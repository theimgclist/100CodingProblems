"""
	Created by Avinash on 11th Jan, 2017
"""

from sys import maxsize
def maxsumsubarray(data,n):
	maxsum = globalsum = data[0]
	for i in range(1,n) :
		maxsum = data[i] if data[i] > data[i] + maxsum else  data[i] + maxsum
		globalsum = globalsum if globalsum > maxsum else maxsum
	return globalsum

if __name__ == "__main__" :
	data = [-2,-3,2,-1,-2,-1,-5,-3]
	sum = maxsumsubarray(data,len(data))
	print(sum)
