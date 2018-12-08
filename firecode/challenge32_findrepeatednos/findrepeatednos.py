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

