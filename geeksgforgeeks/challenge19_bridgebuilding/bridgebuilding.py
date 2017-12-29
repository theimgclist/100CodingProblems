"""
	Created by Avinash on 29th Dec, 2017
"""
	
def bridgebuilding(pairs,n):
	bridgecount = 0
	bridge = [1 for i in range(n)]  # initially, for every pair, length of chain will be 1
	for i in range(1,n): # this loop is for the leading/ending node
		for j in range(0,i):  #this loop is for the beginning node
			if pairs[i][0] > pairs[j][1] and bridge[i] < bridge[j] + 1 :
				bridge[i] = bridge[j] + 1
	for i in range(n):
		if bridgecount < bridge[i] :
			bridgecount = bridge[i]
	return bridgecount

cities = [[6,2],[4,3],[2,6],[1,5]]
cities.sort(key=lambda x: x[0]) #sorting the list of lists based on the 1st element of each list
print(cities)                   # lambda func simply returns the element at index 0 of every inner list
print("Maximum number of bridges that can be built for given cities is %d"%bridgebuilding(cities,len(cities)))
