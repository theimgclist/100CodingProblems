[http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/]	
Given a set of numbers, we should check if it can be split into two subsets of same total.	
If sum of set is K, then we should split S into S1 and S2 such that S1 = S2 = K/2.	
We take a 2D array to contain boolean matrix.	
Our approach is to take K/2 and see if there is any subset that equals to K/2.	
If such subset exists, then there will be another subset of same total K/2 since K is total of entire set.	
We have rows from 0 to K/2 + 1 and columns from 0 to n+1.	
When i = 0, i.e sum = 0, we have null set of all subsets. So first row will be initialized to True.	
When the subset is an empty set, then no sum can be obtained except 0. So the first column is initialized to False.	
Except in the first row, since sum of 0 can be obtained with empty set.		
FOr any index i,j in the boolean matrix, i refers to the total k and j refers to subset until index j.	
Cell i,j is True if there exists a subset Sj whose total is equal to i, False otherwise.	
So the cell at right bottom most row, will have True if the given set has a subset which sums to K/2.	
