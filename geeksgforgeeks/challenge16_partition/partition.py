"""
	Created by Avinash on 19th Dec, 2017
"""

def process():
	n = int(input("Enter the number of elements in set "))
	set = []
	print("Enter the elements of set ")
	for i in range(0,n):
		set.append(int(input()))
	bool = isBiPartitionPossible(set,n)
	if bool :
		print("The given set can be bi partitioned")
	else :
		print("The given set can't be bi partitioned")	

def isBiPartitionPossible(set,n):
	total = sum(set)  
	k = int(total/2)
	partition = [[False for j in range(0,n+1)] for i in range(0,k+1)]
	if total % 2 != 0 :
		return False
	for i in range(0,n+1):
		partition[0][i] = True
	for j in range(1,k+1):
		partition[j][0] = False

	for i in range(0,k+1):
		for j in range(1,n+1):
			if i - set[j-1] >= 0 :
				partition[i][j] = partition[i][j-1] or partition[i-set[j-1]][j-1]
			else :
				partition[i][j] = partition[i][j-1]
	return partition[k][n]	

if __name__ == "__main__":
	process()