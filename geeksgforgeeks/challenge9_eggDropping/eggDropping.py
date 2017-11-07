# Created by Avinash on 6th Nov, 2017
import sys
def process():
	n = int(input("Enter the number of eggs : "))
	k = int(input("Enter the number of floors : "))
	threshold = eggsThresholdFloorCache(n,k)
	print("The threshold floor for given eggs is %-5d" %threshold)

def eggsThresholdFloor(n,k):
	if k == 0 or k == 1 :
		return k
	if n == 1 :
		return k
	min = sys.maxsize
	for j in range(1,k + 1) :
		threshold = max(eggsThresholdFloor(n - 1, j - 1),eggsThresholdFloor(n,k - j))
		if(threshold < min) :
			min = threshold
	return min + 1

def  eggsThresholdFloorCache(n,k) :
	threshold = [[0 for x in range(k+1)]for x in range(n+1)]
	for i in range(1, n+1):
		threshold[i][1] = 1
		threshold[i][0] = 0
	for j in range(1, k+1) :
		threshold[1][j] = j
	for i in range(2, n+1):
		for j in range(2, k+1):
			threshold[i][j] = sys.maxsize
			for x in range(1,j+1) :
				res = 1 + max(threshold[i-1][x-1],threshold[i][j-x])
				if res < threshold[i][j]:
					threshold[i][j] = res
	return threshold[n][k]	
					

if __name__=="__main__":
	process()
		
			