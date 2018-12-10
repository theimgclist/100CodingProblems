# [Binary Representation](https://www.firecode.io/pages/explore/309494)  

**Problem** :

Write a function to compute the binary representation of a positive decimal integer. The method should return a string(Do not use in-built bin() function).  

**Example** :

dec_to_bin(6) ==> "110"  
dec_to_bin(5) ==> "101"  

| Input        | Expected Result           |    
| ------------- |:-------------| 
5 | 101 |  
1 | 1 |  
15 | 1111 |  
2  | 10 |  

**Solution** :  

* Given a decimal number, to get its binary representation, STEP 1. the given decimal number should be divided by 2(since our target system is binary).  STEP 2. The remainder will be appended to the binary representation(which is initially empty) and step 1 and 2 are repeated using the quotient from the previous division  
* Repeat steps 1 and 2 until the number is reduced to less than 2  

**Code** :

Recursive solution :

```Python
def dec_to_bin(n):
    if n<2: return str(n)
    else:
        return dec_to_bin(n//2) + dec_to_bin(n%2)
```

Non-recursive solution :  

```Python
def dec_to_bin(n):
    binary = ""
    while number != 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary
```

One liner solution :

```Python
def dec_to_bin(number):
    return str(number) if number < 2 else str(dec_to_bin(number//2)) + str(dec_to_bin(number%2))
```

**Notes** :  

n/2 vs n//2 - Using **/** will perform floating point division whereas **//** will perform floor division.  
10/2 gives 5.0 whereas 10 // 2 gives 5  
