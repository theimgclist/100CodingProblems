[http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/]   
We are given an amount n.  
We are close given m coins each of denomination c1,c2..cm.  
We can use any number of each of those coins to form the amount equal to n.  
Our task is to find the total number of ways we can make an amount of n using the m coins.  
Let us say the amount or n value is 10.  
We are given 3 coins of denominations 1,2,3.  
To make an amount of 10 using those given coins, we can start with denomination 1.  
We take two coins of denomination 1. So we now have an amount of 2, with 8 still required.  
What if we started with denomination 2? After using one coin of denomination 2, we will still have 8 more to go.  
So taking 2 coins of denomination = 1, we still have  n = 8.  
That means, we have overlapping sub problems.  
This problem also has optimal sub structure.  
Because on taking one denomination = 3,the problem gets reduced to n = 7.  
Suppose the n value is 5 and the denominations are 1,2,3.  
let us first start with only one coin, m = 1.  
With m = 1, we have one way of having n = 5, by having 5 of those.  
When we have m = 1, 2 we have two scenarios.  
You either use the denomination = 2 or you dont.  
When we use it, the problem gets reduced to n = 5 - 2 = 3.  
If we dont use m = 2, then the problem gets reduced to n = 5 and m = 1 which we have already solved.  
The denominations dont necessarily start from 1. They can be any values and they can be in any order.  
We will need m number of rows and n+1 number of columns.  
We need one extra column to hold the results when n = 0(the first column can be filled with 1s before going on to fill the other cells in table).  
  
  


