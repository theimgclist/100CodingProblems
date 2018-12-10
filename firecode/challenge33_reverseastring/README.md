**Problem** :  
Write a function that takes in a string and returns the reversed version of the string.  
**Example** :  
 reverse_string("abcde") -> "edcba"  
reverse_string("1") -> "1"  
reverse_string("") -> ""  
reverse_string("madam") -> "madam"  
**Solution** :  
 There are different ways to do solve this problem. We can use Python's reversed() method.   
 * Instead of using a built-in method, it's better to solve using our own code  
 * One quick way to solve this is to start at the end of the string and then loop over each character till the index 0  
 * This can be easily done using slicing(extended slicing as mentioned in Firecode)

```Python
def reverse_string(a_string):
    return a_string[::-1]
```
* a_string[::-1]  <-> **string[start:stop:step]**
* Another solution from Firecode:
``` Python
def reverse_string(a_string):
    str = list(a_string)
    for i in range(len(a_string)/2):
        str[i], str[-i-1] = str[-i-1], str[i]
    return ''.join(str)
```
* In this solution, the string is first converted to a list since the strings are immutable and can't be directly indexed and modified  

