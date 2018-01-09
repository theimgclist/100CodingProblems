[https://www.geeksforgeeks.org/ugly-numbers/]		
The numbers whose primary factors are only 2,3,5 are called ugly numbers.	
One way to solve this problem is to start with 1, maintain a counter that counts the ugly numbers.	
Keep iterating over the numbers until the required nth ugly number is found.	
For every number do the following :	
If the number is 150, we start by dividing it with 2.	
We get 75, which is not divisible by 2, so we pass 75 for dividing with 3.	
On dividing 75 with 3,we get 25 which is not divisible by 3.	
So we pass 25 for division with 5.	
We get 5 on dividing 25 by 5.	
Since 5 is divisible by 5, we do it one more time.	
Since the final dividend is 1, we take 150 as an ugly number.	
The other way to solve this problem is explained below :	
This is what I used in the code.	
Add 1 to the ugly numbers list.		
Have 3 indices for tracking the numbers 2,3,5.	
In this approach, we use the multiples of 2,3,5 to arrive at a solution.	
We start by taking the minimum value of next multiple of prime numbers 2,3,5 and adding it to the list.		
Since the minimum will be 2 for the multiples 2,3,5 we add 2 to ugly list.	
Since we picked a multiple of 2, we increment i2, which is the tracker we declared for prime number 2.	
Here we also update next multiple of 2 which becomes 4.		
The next min value for available multiples 4,3,5 is 3.		
So we add 3 to the ugly list, increment the i3 tracker and update next multiple of 3 to 6.	
Repeat this for all i until n is reached.	
Return the last element of ugly list which contains the nth ugly number.	