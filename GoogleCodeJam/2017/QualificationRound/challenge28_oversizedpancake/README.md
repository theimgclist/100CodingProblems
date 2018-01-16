[https://code.google.com/codejam/contest/3264486/dashboard#s=p0&a=0]      
This is a problem from Google Code Jam's qualification round for the year 2017.    
Given S number of pancakes and each pancake having one of two states, either happy or blank, we have to flip the pancakes in such a way that all the pancakes are in happy state.     
The constraints for accomplishing the task are as follows:     
The flipper used to flip the pancake is of capacity k(strictly).   
At any instant, it can't flip pancakes that are less than k.   
Since each pancake has one of two states and our goal is to convert them all into happy state(if possible), we start from the left end and consider pancakes that are currently not in happy state.    
We start with pancake at index 0. If it's in happy state already, we continue to next.    
If its not in happy state, we flip it.   
And by doing so, we flip the k number of pancakes starting at 0.   
Let's take an example input : S = ---+-++- , K = 3   
Here - denotes blank state and + denotes happy state.   
We start with index 0. Since it  is a blank state, we do a flip operation at index 0.   
This will flip the first 3 pancakes and we now have ++++-++-.   
We then iterate through the next pancakes until we find a blank state.     
Our next blank state is at 4.   
On performing flip operation at 4, we will get +++++---.    
We then search for next blank state which is at 5 and perform flip.   
This will give us ++++++++ which is our final state.   
In this example the number of flips are 3.   
For cases where it's not possible to get all happy states, we simply return IMPOSSIBLE.    
