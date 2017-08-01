def process() :
	data1 = input("Enter the first string : ")
	data2 = input("Enter the second string : ")
	distance = editDistance(data1, data2)
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

	
if __name__=="__main__":
	process()	