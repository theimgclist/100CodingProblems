[https://code.google.com/codejam/contest/3264486/dashboard#s=p2&a=2]    
We are given a row of stalls in a bathroom.   
Two stalls at both ends of the row are always occupied.   
When a person goes to bathroom and wants to choose one stall S, there are two constraints that have to be met.  
Stall S should be chosen in such a way that, it is farthest from any of the occupied stalls.   
For example, lets say the current state is X000X0X0X where X represent occupied stall and 0 represent free stall.   
For a person going next, there are 5 free stalls.   
Among those, the one at the index 3 has to be chosen since among all free stalls, it is the one that is farthest from an occupied stall.   
So now the state becomes X0X0X0X0X.   
We have two values LS and RS. LS is the number of unoccupied stalls between the current stall S and the nearest occupied stall on its left.     
RS is the number of unoccupied stalls between the current stall S and the nearest occupied stall on its right.  
So for every unoccupied stall, there will be a pair of calculated values LS and RS.   
We take the list of minimum value from each pair and find the maximum value from the list.  
This will give us the index of the next stall that has to be chosen.  
If there is a tie i.e we have more than one index that equals max value, we then check the max values only for those pairs and pick the max value as the index.  
Here is one example where number of stalls N = 6 and number of people K = 3.   
Initial state -> X000000X  (X at both ends are the always occupied stalls)  
For the left most stall S at 1, LS which is how far the closest occupied stall is to S is 0. Since there is one occupied stall right next to S on its left.  
Similarly RS will be 5.  
So for all the unoccupied stalls from left to right, we have the following pairs of LS,RS :
(0,5) (1,4) (2,3) (3,2) (4,1) (5,0).  
The list of min values from each pair will be [0,1,2,2,1,0].   
Now we need the max value from the list which is 2.  
Since we have a tie here for the pair 2,3 and 3,2 we take the max value for each and then maximize it.  
For 2,3 and 3,2 list of max values will be [2,2] which again is a tie.   
In such cases, we take the unoccupied stall which is towards the left.  
So the first person takes the stall at index 4.  
State becomes -> X00X000X.  
Now LS,RS pairs will be - (0,1) (1,0) (0,2) (1,1) (2,0).
min list - [0,0,0,1,0]
We have a max value 1 for the min list.  
So we choose that stall which is at index 6.   
Now the stalls state will be -> X00X0X0X.  
For the kth time, we will return max(LS,RS) and min(LS,RS) as the output.   

I overlooked few things from the problem statement because of which I spent more than an hour trying to solve it differently and in a wrong way.  
Attention is very important when reading the problem statement.   
We can use max heap to solve this problem.  
For every new person, we should find the longest continguous unoccupied stalls and that count can be stored in a maxheap.  
So if number of stalls are 100, after the first person occupies the stall at index 50, we will have 49 on left and 50 on right.  
We push that count to a maxheap which returns the max value when we later pop it.  
We then pick the right side since it has more unoccupied stalls(50 vs 49).   
The next person occupies the 25th stall between 51 and 100.   
That will give us another 2 contiguous stalls of 24 and 25.  
We will push those into the maxheap.   
The next pick will be from left where there are 49 unoccupied stalls.   
This is done until we allot stalls for all K people.  


  
