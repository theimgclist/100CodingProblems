[https://code.google.com/codejam/contest/3264486/dashboard#s=p1]     
Given a number N, problem is to find the last or the largest tidy number in the range of 1 to N.   
What is a tidy number?   
A tidy number is one in which its digits from left to right are in non-decreasing order.   
For example 12345, 489, 777, 9, 12 are all tidy numbers whereas 213, 101, 981 are not.   
One of the naive ways to try this problem is to iterate through every number in the range 1 to N, have a method that checks if the number passed to it is a tidy number.     
If yes, set it to a variable that holds the largest tidy number so far.   
We will be needing each digit of the numbers we iterate through.   
Though a workable solution can be obtained with this naive approach, for large datasets where N can be as big as 10^18, it is just not efficient.   
Let us try an example - 132.   
We first check if N is already a tidy number.   
Since it's not non decreaasing, N is not a tidy number.   
The last/largest tidy number between 1 and 132 is 129.   
How can we efficiently arrive at that solution?   
As we see, the problem we have is with the digits 3 and 2 which are decreasing as we go from left to right.   
Let's call that an inverse. So we start with finding an inverse.  
For N = 132, we know the largest tidy number is 129.   
The inverse happened at digit 3 which is at index 2(let's have 1-indexed array).  
Since we know 132 is not a tidy number, the required tidy number will be some number < 132.   
Since inverse is the problem we have here, handling it might give us our tidy number.  
By changing 3 to 2, we will have 122 and the inverse is killed!  
Though 122 itself is a tidy number, its not the tidy number we need.  
After resolving the inverse, we should also see if the number can be further maximised.   
Which we can do by changing the last digit 2 to 9.  
Now that gives us the required tidy number.  
To generalize it for any number :  
1. Find the index i where the inverse happens.    
2. Resolve the inverse by changing the number at i-1(reduce it by 1)   
3. Change all digits from index i+1 till the end to 9.   
Step 2 will have some special cases to consider. What if the change leads to another inverse?   
In that case, we will leave the digit as is, and check the one before it.  
For example, when N = 5775, we see the inversion at i = 3.  
Though we can resolve this inverse by taking 5765, this again has an inverse.  
So we avoid that step and directly go to 7 at index 2.  
Now reduce the digit by 1 and add 9s to fill the remaining digits.  
This will give us 5699.   