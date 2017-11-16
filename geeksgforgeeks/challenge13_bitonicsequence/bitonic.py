# Created by Avinash on 16th Nov, 2017
import sys
def calculate_bitoniclen(n, data):
	lisCount = [1] * n
	ldsCount = [1] * n

	for i in range(1, n):
		for j in range(0, i):
			if data[i] > data[j] and lisCount[i] < lisCount[j] + 1 :
				lisCount[i] = 1 + lisCount[j]

	for i in range(n-2, 0, -1):
		for j in range(n-1, i, -1):
			if data[i] > data[j] and lisCount[i] < lisCount[j] + 1 :
				ldsCount[i] = 1 + lisCount[j]

	bitonic = lisCount[0] + ldsCount[0] -1
	for i in range(1, n):
		 if lisCount[i] + ldsCount[i] - 1 > bitonic: 
		 	bitonic = lisCount[i] + ldsCount[i] - 1
	return bitonic	
	 

def process():
	n = int(input("Enter the number of elements in data : "))
	data = []
	print("Enter the actual data ")
	for i in range(0, n):
		data.append(int(input()))
	bitonic = calculate_bitoniclen(n,data)	
	print("The length of bitonic subsequence for the given data of numbers is : %-5d" %bitonic)
	
if __name__=="__main__":
	process()