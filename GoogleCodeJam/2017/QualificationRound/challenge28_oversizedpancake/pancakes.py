"""
	Created by Avinash on 16th Jan 2017
"""
def pancakeflips(S,K) :
	k = int(K)
	pancount = len(S)
	s = [ x == '+' for x in S]
	flipcount = 0
	for i in range(pancount - k + 1) :
		if not s[i] :
			for j in range(i, i + k) :
				s[j] = not s[j]
			flipcount += 1
	return flipcount if all(s) else "IMPOSSIBLE"	


import fileinput
read = fileinput.input()
testcases = int(read.readline())
for testcase in range(1,testcases+1) :
	S, K = read.readline().split()
	flips = pancakeflips(S,K)
	print("Case #{}: {}".format(testcase,flips))


	

		
	