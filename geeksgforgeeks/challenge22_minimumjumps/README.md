[https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/]		
Given an array of numbers, where numbers at each index says how many steps ahead can be taken from the current index, goal is to reach the end in minimum jumps.	
For example, for the data - 1, 3, 5, 6, 3, 2, 6, 7, 6, 8, 9, the minimum number of jumps required is 4.		
1 -> 3 -> 5 -> 7 -> 9.
We initialize jumps[] array which contains the number of jumps to reach end from each index, to zero. 	
We can traverse both from left to right or from the other way.		
Starting from right end and the second last element at index n-2, we check if end is reachable.  	
If yes, we increment jumps[n-2] by 1.		
We go to the next element at index n-3 and see if end is reachable.	
If any index holds  the value 0, that means we can't go ahead through that index. 	
So jumps[] for that index will be 0.	
This way, we traverse through all elements until we reach index 0 and find how many jumps it takes to reach end from there.	
