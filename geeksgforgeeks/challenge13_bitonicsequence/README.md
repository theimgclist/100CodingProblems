[http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/]		
This problem can be solved using longest increasing subsequence.	
This is how we find the longest increasing subsequence for a given array of numbers.	
For every index, the length(L) of LIS will be initially 1.		
For index 0, L will be 1.		
We then add one element at a time to the sequence.		
Element at index 1 is added and we check if the new element is greater.		
If yes, then we increment L by 1.	
When a 3rd element is added, we start at index 0 again and do the check if new element is greater than the element at index 0 and index 1.		
So for every new element we add to check, we should start with index 0.		
Why cant we use the L value of previous element?	
For some problems , we see that the computing value for a new element added to list can be derived using the last computed value.  
But in this problem, the LIS may or may not contain the last computed element.  
So we should check for all elements.  
To calculate bitonic sequence, we use LIS.  
