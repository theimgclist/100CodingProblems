def optimalBST(keys,freq,n):
	cache = [[ 0 for j in range(n)] for i in range(n)]
	for i in range(n):
		cache[i][i] = freq[i]
	for sub in range(2,n+1): 	
		for i in range(0,n-sub+1): 
	 		j = i + sub - 1   
	 		cache[i][j] = float("Inf")
	 		total = sum(freq[i:j + 1])
	 		for r in range(i,j+1):
				val = total + (0 if r - 1 < 0 else cache[i][r - 1]) + (0 if r + 1 > j else cache[r + 1][j])
				cache[i][j] = min(val,cache[i][j])
	return cache[0][-1]	
	
	
	
if __name__=="__main__":
	keys = [10,12,20]
	values = [34,8,50]
	result = optimalBST(keys,values,3)

