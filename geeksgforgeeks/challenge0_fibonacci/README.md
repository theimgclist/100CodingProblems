[http://www.geeksforgeeks.org/dynamic-programming-set-1/]  
I have chosen Dynamic Programming as the algorithmic paradigm from GeeksforGeeks for solving coding challenges.  
In Fibonacci sequence(0,1,1,2,3,5 and so on), the first 2 items are 0,1 and the subsequnet item is formed by adding the 2 items prior to it.  
So, the nth Fibonacci number is derived by adding n-1 and n-2 terms.  
This is a very good example of **Overlapping Subproblems** property, which is one of the properties of DP.  
There are multiple ways to derive a Fibonacci sequence of **n** numbers:  
   1. Memoization- since the naive recursion is very slow and not optimal, we can use memoization(Top down approach)  
   2. Tabulation - this uses bottom up approach where all the possible values  for i(i <= n) are calculated  
Though this is a pretty straight forward problem, I got stuck a couple of times.  
Take care of the boundary values of the for loops used,as per the requirement, to avoid index out of bounds exception.  
Use BufferedReader instead of Scanner since it is faster.  
For knowing more about better ways of I/O in java, check the URL:[http://www.geeksforgeeks.org/fast-io-in-java-in-competitive-programming/]  
This is the first problem i solved in Python after a long time(around 3 years) and it took so long considering it is Fibonacci which i tried.  
While passing **n** value to the methods that solve Fibonacci, i reduced its value by 1 before passing.  
The nth term in the actual Fibonacci sequence, will be the same as the (n-1)th term in our list that contains the Fibonacci numbers.  
It is because, the list or table we use to save the numbers is 0 indexed. So we should either pass (n-1) value to the method or return the value at index (n-1) to the calling method.
