[https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/]	
Given an array of numbers, we should find the congiguos sub array such that, it has the maximum total.	 
There are different ways to solve this problem.	  
One approach is Brute force, generate all sub arrays and see which of those has the maximum sum.	
This is not efficient computationally.	 
So we can use Kadene algorithm which helps us solve the problem in O(n).	 
We first add the first element's value as the best max sum possible.	
Lets say we have the array 2,-1,6,7,8.	
WE start by setting maxsum to 2, the first element in array.	
We next take the max of last element's maxsum and the new element.	
max(2, 2 + (-1)) -> 1.	
Our maxsum remains the same for the first 2 elements.	 
We now take the next value which is 6.	 
max(6, 6 + 1) -> 7.	
For element 7, the max(7,7+7) will be 14.	
Similarly after adding element 8, max(8,8+14) will be 22.	
We can declare maxsum either as an array variable or a normal single valued variable.	
If array is taken, we should find the max of all the array values to return the maxsum. 	
Though that is correct, it needs unnecessary space. 	
To avoid that, for every value, we can check maxsum with globalsum and update globalsum everytime a new maximum sum is obtained.  	
[http://theoryofprogramming.com/2016/10/21/dynamic-programming-kadanes-algorithm/]    
Besides Geeksforgeeks, the above link also explaines Kadene algorithm with a good example.  	
