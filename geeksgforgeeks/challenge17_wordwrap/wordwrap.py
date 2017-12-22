"""
   Created by Avinash on 20th Dec, 2017
"""
import sys
def process():
	text = input("Enter the text ")
	lineWidth = int(input("Enter the line width "))
	formattedText = wordWrap(text,lineWidth)

def wordWrap(text,width) :
	words = text.split()
	print(words)
	count = len(words)
	cost = [[0 for j in range(count)] for i in range(count)] # 2D array for storing cost of different words in a line
	for i in range(count):
		cost[i][i] = width - len(words[i]) # cost of adding only one word in the line
		for j in range(i+1,count):
			cost[i][j] = cost[i][j-1] - len(words[j]) - 1 # adding multiple words per line
	for i in range(count):
		for j in range(i,count):
			if cost[i][j] < 0 :
				cost[i][j] = sys.maxsize
			else :
				cost[i][j] = cost[i][j] ** 2  # penalizing the extra spaces
	minCost = [0 for i in range(count)]
	result = [0 for i in range(count)]
	for i in range(count-1,-1,-1): # for every ith iteration, we take the words from i till last word
		minCost[i] = cost[i][count-1]
		result[i] = count # contains the index of word which can be printed in one line from ith word 	     
		for j in range(count-1,i,-1):
			if cost[i][j-1] == sys.maxsize : # if one/every word length exceeds width,result[] will contain same value at many/all indices
				continue                 # make width = max(words.length) to handle the issue
			if minCost[i] > minCost[j] + cost[i][j-1] :
				minCost[i] = minCost[j] + cost[i][j-1]
				result[i] = j
	print("Minimum cost is %d"%minCost[0])
	printText(words,result)
		
def printText(words,result) :
	count = len(words)
	i = 0
	data = ""
	firstIter = True
	while firstIter or j < count :
		j = result[i]
		for k in range(i,j):	
			data += words[k] + " "
		data += "\n"
		i = j
		firstIter = False
	print(data)	
	
if __name__ == "__main__" :
	process()