def process() :
	print("Enter the dimensions of cost matrix : ")
	m = int(input())
	n = int(input())
	cost = [[0]*(m) for i in range(n)]
	print("Enter the costs : ")
	for i in range(m) :
		for j in range(n) :
			cost[i][j] = int(input())
	print("Enter the co ordinates of destination : ")
	x = int(input())
	y = int(input())
		
	#distance = editDistance(data1, data2)
	minCost = minCostPath(cost, x,y)
	print("The minimum cost it takes is : %-5d" %minCost)
	
def minCostPath(cost, x, y) :
	cache = [[None]*(x + 1) for i in range(y + 1)]
	for i in range(x + 1):
		for j in range(y + 1):
			if i == 0 and j == 0 :
				cache[i][j] = cost[i][j];
			elif i == 0 :
				cache[i][j] = cache[i][j-1] + cost[i][j];
			elif j == 0 :
				cache[i][j] = cache[i-1][j] + cost[i][j];
			else :
				cache[i][j] = cost[i][j] + min(cache[i-1][j], cache[i-1][j-1], cache[i][j-1])
	return cache[x][y]

	
if __name__=="__main__":
	process()	