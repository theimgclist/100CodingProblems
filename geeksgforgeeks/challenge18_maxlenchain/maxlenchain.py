"""
	Created by Avinash on 27th Dec,2017
"""
class Pair(object):
	def __init__(self,a,b):
		self.a = a
		self.b = b
def maxlenchain(pairs,n):
	chainlen = 0
	chain = [1 for i in range(n)]  # initially, for every pair, length of chain will be 1
	for i in range(1,n): # this loop is for the leading/ending node
		for j in range(0,i):  #this loop is for the beginning node
			if data[i].a > data[j].b and chain[i] < chain[j] + 1 :
				chain[i] = chain[j] + 1
	for i in range(n):
		if chainlen < chain[i] :
			chainlen = chain[i]
	return chainlen

data = [Pair(5,24), Pair(15,25), Pair(27,40), Pair(50,60)]
print("Maximum chain that can be formed using the given pairs is %d"%maxlenchain(data,len(data)))
		

	