# Created by Avinash on 14th Nov, 2017
import sys
def calculate_SumOfLIS(n, data):
	lisCount = [1] * n
	lis = 0
	position = -1
	sumlis = [1] * n
	max_sum = 0
	for i in range(0,n):
		sumlis[i] = data[i]
	for i in range(1, n):
		for j in range(0, i):
			if data[i] > data[j] and lisCount[i] < lisCount[j] + 1 :
				lisCount[i] = 1 + lisCount[j]
			if data[i] > data[j] and sumlis[i] < sumlis[j] + data[i] :
				sumlis[i] = sumlis[j] + data[i];	
	for i in range(0, n):
		if lis < lisCount[i]:
			lis = lisCount[i]
			position = i
		if max_sum < sumlis[i]:
			max_sum = sumlis[i]	
	theSequence = str(data[position]) + " "
	result = lis - 1
	for i in range(position - 1, -1, -1):
		if lisCount[i] == result :
			theSequence = str(data[i]) + " " +theSequence
			result -= 1
	return lis,theSequence,max_sum	
	 

def process():
	n = int(input("Enter the number of elements in data : "))
	data = []
	print("Enter the actual data ")
	for i in range(0, n):
		data.append(int(input()))
	lis, sequence, total = calculate_SumOfLIS(n,data)	
	print("The length of longest increasing subsequence for the given data of numbers is : %-5d" %lis)
	print("The longest increasing subsequence is : %s"%sequence)
	print("the sum of longest increasing subsequence is : %s"%total);	
	
if __name__=="__main__":
	process()