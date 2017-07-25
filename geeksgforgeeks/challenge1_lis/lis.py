# Created by Avinash on 21st July, 2017
import sys
def calculate_LIS(data):
	lisCount = []
	n = len(data)
	for i in range(0, n):
		max = -1
		for j in range(0, i):
			if data[i] > data[j]:
				if max == -1 or max < lisCount[j] + 1 :
					max = 1 + lisCount[j]
		if max == -1 :
			max = 1
		lisCount.append(max)
	lis = -1
	position = -1
	for i in range(0, n):
		if lisCount[i] > lis :
			lis = lisCount[i]
			position = i
	theSequence = str(data[position]) + " "
	result = lis - 1
	for i in range(position - 1, -1, -1):
		if lisCount[i] == result :
			theSequence = str(data[i]) + " " +theSequence
			result -= 1
	return lis,theSequence	
	 

def process():
	n = int(input("Enter the number of elements in data : "))
	data = []
	print("Enter the actual data ")
	for i in range(0, n):
		data.append(int(input()))
	lis, sequence = calculate_LIS(data)	
	print("The length of longest increasing subsequence for the given data of numbers is : %-5d" %lis)
	print("The longest increasing subsequence is : %s"%sequence)	
	
if __name__=="__main__":
	process()