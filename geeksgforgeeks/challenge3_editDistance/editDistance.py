def process() :
	data1 = input("Enter the first string : ")
	data2 = input("Enter the second string : ")
	#distance = editDistance(data1, data2)
	distance = editDistance_usingLCS(data1, data2)
	print("The number of operations required to transform first string to second is : %-5d" %distance)
	
def editDistance(s1,s2) :
	len1 = len(s1)
	len2 = len(s2)
	if len1 == 0 :
		return len2
	elif len2 == 0 :
		return len1
	cache = [[None]*(len2 + 1) for i in range(len1 + 1)]
	for i in range(len1 + 1):
		for j in range(len2 + 1):
			if i == 0 :
				cache[i][j] = j
			elif j == 0 :
				cache[i][j] = i	
			elif s1[i - 1] == s2[j - 1] :
				cache[i][j] = cache[i-1][j-1]
			else:
				cache[i][j] = 1 + min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])
	return cache[len1][len2]

def editDistance_usingLCS(s1,s2) :
	len1 = len(s1)
	len2 = len(s2)
	lcs = [[None]*(len2 + 1) for i in range(len1 + 1)]
	for i in range(len1 + 1):
		for j in range(len2 + 1):
			if i == 0 or j == 0 :
				lcs[i][j] = 0
			elif s1[i - 1] == s2[j - 1] :
				lcs[i][j] = 1 + lcs[i-1][j-1]
			else:
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
	length = lcs[len1][len2]
	return max(len1-length, len2-length)

	
if __name__=="__main__":
	process()	