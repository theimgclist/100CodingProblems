"""
	Created by Avinash on 17th Jan 2018
"""
def findtidynumber(n):
	digitcount = len(n)
	if(digitcount == 1) : # when there is only one digit in the number, it's a tidy number
		return n
	elif(all(x == n[0] for x in n)) : # when all digits in number are same, it's a tidy number
		return n
	else :
		lastdigit = "0"
		for i, digit in enumerate(n) :
			if digit < lastdigit :  # if a inverse happens
				prefix = str(int(n[:i])-1)  # reduce the i-1 digit by 1
				suffix = (digitcount - i) * "9"  # fill the remaining digits with 9s
				return findtidynumber(prefix+suffix) # recursively find the tidy number for updated number
			lastdigit = digit  # keeping track of the previous digit
	return int(n) # if not converted to int, number will be returned with trailing 0s if any	
			


import fileinput
read = fileinput.input()
testcases = int(read.readline())
for testcase in range(1,testcases+1) :
	N = read.readline().strip()
	tidynumber = findtidynumber(N)
	print("Case #{}: {}".format(testcase,tidynumber))	