[https://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/]		
We are given n boxes, each with dimension D(height,length,width).		
We have to stack the boxes in such a way that maximises the height of the stack.	
Boxes can be stacked on a condition that, a box can be stacked on top of another box,only when the base area of the new box is less than that of the one below.		
The boxes can be rotated and used with rotated dimensions.	
This problem can be solved using LIS.	
Find the permutation of all possible dimensions.	
Sort them using the base area.		
On the sorted boxes, apply LIS.		
