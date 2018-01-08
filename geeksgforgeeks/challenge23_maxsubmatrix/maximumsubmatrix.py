"""
	Created by Avinash on 8th Jan, 2017
"""
def maxsubmatrix(data) :
	rows = len(data)
	columns = len(data[0])
	sub = [[0 for j in range(columns)] for i in range(rows)]
	dim = sub[0][0]
	for i in range(1,rows):
		for j in range(1,columns):
			if(data[i][j] == 1):
				sub[i][j] = min(sub[i][j-1],sub[i-1][j],sub[i-1][j-1]) + 1
			else :
				sub[i][j] = 0

	dim = sub[0][0]
	dim_i = 0
	dim_j = 0
	for i in range(rows):
		for j in range(columns):
			if(dim < sub[i][j]) :
				dim = sub[i][j]
				dim_i = i
				dim_j = j
	print("Here is the maximum square sub matrix of size %d "%dim)
	for i in range(dim_i, dim_i - dim, -1):
		for j in range(dim_j, dim_j - dim, -1):
			print(data[i][j], end = " ")
		print("")	

if __name__ == "__main__" :
	data = [[0,1,1,0,1],
		[1,0,0,1,0],
		[0,0,1,1,0],
		[1,1,1,1,0],
		[1,1,1,1,1],
		[0,0,0,0,0]]
	maxsubmatrix(data)	