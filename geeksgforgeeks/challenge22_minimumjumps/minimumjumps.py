"""
	Created by Avinash on 7th Jan, 2017
"""
def minimumjumps(data,n) :
	jumps = [0 for i in range(n)]
	for i in range(n-1,-1,-1) : # start from right end and traverse to left
		if data[i] == 0 : # when no steps can be taken any further from index i
			jumps[i] = float('inf')
		elif data[i] >= n-i-1 : # when end can be reached directly from i
			jumps[i] = 1
		else :
			min = float('inf')
			for j in range(i+1,n): # when end can't be reached directly from i, check all reachable indices from i
				if j <= data[i] + i : # restrict j till where you can reach from i
					if min > jumps[j] : # take min of all jumps that can reach to end
						min = jumps[j]
			if min != float('inf') :
				jumps[i] = min + 1
			else :
				jumps[i] = min	
	return jumps[0]



if __name__ == "__main__" :
	data = [1, 3, 5, 6, 3, 2, 6, 7, 6, 8, 9]
	n = len(data)
	print("Minimum number of jumps to reach the end is %d"%int(minimumjumps(data,n)))
		