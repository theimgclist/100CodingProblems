[https://www.geeksforgeeks.org/dynamic-programming-building-bridges/]		
Remember to pay attention while you read the problem statement.		
You misunderstand one word or instruction, you will end up trying to find a solution to an unasked problem.		
Given that there is a river flowing through center of a region and n cities on either sides of it.		
The X co-ordinates of each city on one side(north lets say) are given.		
Similarly, the X co-ordinates of each city on the other side(south) are also given.		
We take two arrays of size n each(N and S) such that, a bridge can be constructed from city N[i] to S[i].		
There is a condition for bridge building. We have to maximize the bridges, that is build as many bridges as possible meeting the condition that no two bridges cross each other.		
As mentioned already, we are given co-ordinates of each city.		
City 1 can be at co-ordinate 5 and city 10 can be at co-ordinate 2.		
There is no order or relation between city number and its X co-ordinate.		
This problem can be solved using two steps.		
Take the south cities co-ordinates and sort them.		
Align the north cities in line with their corresponding south cities.		
Find the longest increasing subsequence for north cities co-ordinates.		
That will give us the number of bridges that can be built without any two of them crossing each other.		
Let us start with first city. It is at some co-ordinate x at south end and we will connect it with its corresponding city at y.	  	
We then consider adding the next city. As per the condition, we can build another bridge or link, only when its corresponding city is on the right side of y, which means, it has to form an increasing sequence with prior y.		
That's nothing but finding the longest increasing subsequence.		
__repr__() is a default method which gets executed for a class. It can be overwritten for changing the structure of how a class gets printed.		
Spent more than an hour trying to know different ways of sorting.		
Sorting a list, list of lists, list of objects.		
The solution to this problem is similar to maximum chain length of given pairs of integers.		
Instead of using a class approach, I removed the object implementaion and solved it directly using array indexing.		
