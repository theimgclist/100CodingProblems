def optimalBST(keys, freq, n):
    cache = [[ 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        cache[i][i] = freq[i] # when there is only one node
    for sub in range(2,n+1): # picking nodes of different length >= 2
        for i in range(0,n-sub+1):  # gives the starting index of current sequence of nodes
            j = i + sub - 1   # gives ending index of current sequence of nodes
            cache[i][j] = float("Inf")
            total = sum(freq[i:j+1])
            for r in range(i,j+1):  # picking different nodes
                val = total + (0 if r-1 < 0 else cache[i][r-1]) + (0 if r + 1 > j else cache[r+1][j])
                cache[i][j] = min(val,cache[i][j])
    return cache[0][-1]


if __name__ == "__main__":
    keys = [10,12,20]
    values = [34,8,50]
    result = optimalbst(keys, values, 3)
    print(result)

