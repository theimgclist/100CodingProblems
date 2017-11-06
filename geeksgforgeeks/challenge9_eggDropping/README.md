[http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/]  
Here we have 2 inputs, number of eggs N and number of floors K.  
The base cases will be N = 1 for some value of K and K = 1 for some value of N.  
When there is only 1 egg available, it might break in the 1st floor or in the last floor. Since we are taking the worst case, it will be N.  
Where there are K eggs and only one floor, the number of trials will be one, since in our 1st attempt itself it will be known whether the egg breaks or not.  

