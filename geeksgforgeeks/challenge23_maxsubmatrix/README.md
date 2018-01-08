[https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/]		
Given a matrix of dimensions row X columns, problem is to find the max square submatrix with every element = 1.		
This can be solved with a typical DP approach using the table.		
While filling out the result table, check for the elements at indices - (i,j-1), (i-1,j), (i-1,j-1).		
We then take the minimum of the 3 elements, add 1 to it and save it at the index (i,j).		
The dimension of the maximum square sub matrix will be the maximum value in the result table.				
Using that value and the index of it, we can trace the square matric and print.		