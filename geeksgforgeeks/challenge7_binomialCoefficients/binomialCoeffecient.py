# Created by Avinash on 1st Sept, 2017
def process():
	n = int(input("Enter the value of n "))
	k = int(input("Enter the value of k "))
	coeff = binomialCoeff(n,k)
	print("The binomial coefficient is %-5d" %coeff)
	
def binomialCoeff(n,k):
	m = [[0 for x in range(k+1)] for x in range(n+1)]
	for i in range(n+1):
		for j in range(min(i,k)+1):
			if j == 0 or j == i:
				m[i][j] = 1
			else:
				m[i][j] = m[i-1][j-1] + m[i-1][j]
	return m[n][k]
	
if __name__=="__main__":
	process()