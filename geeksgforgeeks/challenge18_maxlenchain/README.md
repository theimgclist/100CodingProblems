[https://www.geeksforgeeks.org/dynamic-programming-set-20-maximum-length-chain-of-pairs/]		
This problem can be solved using the algorithm for longest increasing subsequence.		
There are N pairs, first element of each pair is smaller than the second.	
Goal is to find the longest chain that can be formed such that :		
if A(x1,x2) and B(x3,x4) are two pairs, they can form a chain as AB only when x2 < x3.		
We have an array CHAIN to store the length of longest chain for a sequence of pairs.		
Initially, CHAIN is set to 1, since for every individual pair, length = 1.		
For every pair at index i, we check for the above condition with all the preceeding pairs.		
Whenever the condition is met, we increment the value by 1.		
We compare the pair at index 1 with 0, if condition evaluates to true, increment CHAIN[1].		
The inpur is an array/list of pairs.	
I started with two arrays, one for 1st elements in all pairs and an other array for 2nd elements in all pairs.		
I thought of zipping them to form a dictionary of pairs.	
But that didnt seem right, so i tried GFK approach.		