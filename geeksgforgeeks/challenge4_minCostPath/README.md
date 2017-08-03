[http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/]   
We have a cost matrix, which says the cost of each node.  
Given a node N with coordinates (x,y), we should find the path with minimum cost from node at (0,0) to (x,y).  
The first row and first column can be filled in at first, since these nodes can be reached in only one way.  
We then keep finding the minimum cost paths for all nodes, until we reach our destination node.  
