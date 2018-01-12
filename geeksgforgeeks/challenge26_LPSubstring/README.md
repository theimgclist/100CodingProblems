[https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/]	  
The problem is, given a string, we should find the longest palindromic substring in it.		
It can be solved in a similar way to longest palindromic subsequence.  	
However, there is a slight difference.	 
substring vs subsequence - for a string codingiscool, "oding" "iscool" "ingis" are examples of substrings.	 
"odis" "inool" "oool" are subsequences.		
The difference is, substrings should be contiguous characters. 	
subsequences need not be contiguous as long as the order of occurence is maintained.	 
To solve the current problem, we use a table of size n X n.	 
If a substring starting at index i and ending at j is a palindrome, then we set table[i][j] to True.	 
All substrings of length 1 are palindromes. So we initialize table[i][i] to 1.	 
We then start for substrings of different lengths >= 2 and see if they are palindromes.	 
In longest palindrome subsequence, even if the first and last elements of current subsequence are not same, we check for the characters within. 	
But in case of longest palindrom substring, for a substring if the first and last elements are not same, then it cant be a palindrome. 		
Everytime the condition check for palindrome is True, we save the substring length in a variable maxlen. 	
After iterating for all substrings, maxlen gives the length of the longest palindromic substring.	 