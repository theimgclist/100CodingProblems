def dec_to_bin_recursive(n):
    if n<2: return str(n)
    else:
        return dec_to_bin_recursive(n//2) + dec_to_bin_recursive(n%2)

def dec_to_bin_nonrecursive(number):
    binary = ""
    while number != 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

if __name__ == "__main__":
    input = int(input("Enter the decimal input "))
    binary = dec_to_bin_nonrecursive(input)
    print("Binary representation of %d " %input + "is %s" %(binary))
    print(binary)