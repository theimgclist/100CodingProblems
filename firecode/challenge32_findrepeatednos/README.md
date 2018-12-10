#### [Repeated Elements in Array](https://www.firecode.io/pages/explore/308951)  
* This problem is from [Firecode.io](https://www.firecode.io/) which I recently came across and it's cool!  
* It's a simple problem -  given a list of numbers, the output should be a sorted list of repeated numbers in the original list
* One way to do this is to sort the original list and start from index 1 and keep iterating through the rest of the list
* As we do this, we compare the current list item with the previous and see if there is a match
* Match indicates a duplicate and the matched number has to be saved for result

Below are some test cases from Firecode:    

| Input        | Expected Result           |    
| ------------- |:-------------|   
| [4]           | [Empty]|
|[1, 3, 3, 4]   | [3] |
|[4, 3, 1]      | [Empty] |
|[1, 5, 23, 2, 6, 3, 1, 8, 12, 3]| [1, 3]|

Below is a solution I came up with:
```Python
"""
    Created by Avinash on 8th Dec, 2018
"""
def duplicate_items(list_numbers):
    list_numbers.sort()
    repeatlist = []
    for i in range(1,len(list_numbers)):
        if list_numbers[i] == list_numbers[i-1]:
            repeatlist.append(list_numbers[i])
    return repeatlist

if __name__ == "__main__":
    result = duplicate_items([1, 5, 23, 2, 6, 3, 1, 8, 12, 3])
    print(result)

```

An other solution:  
```Python
def duplicate_items(list_numbers):
    set_list = set(list_numbers)
    return [i for i in set_list if list_numbers.count(i)>1]
```
* set() gives all the unique values in a list and we can then get the count of each unique item and return those list items whose count is greater than 1
* note that set() by default returns the unique values in a sorted order

