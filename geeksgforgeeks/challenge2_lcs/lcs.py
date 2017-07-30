def process() :
	data1 = input("Enter the first sequence : ")
	data2 = input("Enter the second sequence : ")
	lcs, sequence = calculate_LCS(data1, data2)
	print("The length of longest common subsequence is : %-5d" %lcs)
	print("The longest common subsequence is : %s"%sequence)
	
def calculate_LCS(s1,s2) :
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
	sequence = [None] * (length)
	i = len1
	j = len2
	while i > 0 and j > 0 :
		if s1[i - 1] == s2[j - 1] :
			sequence[length - 1] = s1[i - 1]
			i -= 1
			j -= 1
			length -= 1
		elif lcs[i-1][j] > lcs[i][j-1] :
			i -= 1
		else :
			j -= 1
	return lcs[len1][len2], "".join(sequence)

	
if __name__=="__main__":
	process()	