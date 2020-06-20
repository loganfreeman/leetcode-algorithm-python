def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    cache = [[0 for j in range(n+1)] for i in range(m+1)]
    for i, s1c in enumerate(s1):
        for j, s2c in enumerate(s2):
            if s1c == s2c:
                cache[i+1][j+1] = cache[i][j] + 1
            else:
                cache[i+1][j+1] = max(cache[i][j+1], cache[i+1][j])
    sequence = ""
    i, j = m, n
    while i >=1 and j >= 1:
        if s1[i-1] == s2[j-1]:
            sequence += s1[i-1]
            i, j = i -1, j-1
        elif cache[i-1][j] > cache[i][j-1]:
            i -= 1
        else:
            j -= 1
    return (len(sequence), sequence[::-1])

if __name__ == "__main__":
    print(longest_common_subsequence("ABCXYZ","ACBCXZ"))