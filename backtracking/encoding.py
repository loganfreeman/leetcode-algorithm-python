"""if '*' means repeat from the beginning, what is the mininal characters to encode the string"""
def encode(s):
    n = len(s)
    res = n
    if n == 0:
        return 0
    for i in range(1, n):
        if i * 2 < n:
            if s[0:i] == s[i:i*2]:
                temp = i + 1 + encode(s[i*2:n])
                if temp < res:
                    res = temp

    return res

print(encode('ABCABCD'))
print(encode('ABCABCABCABCD'))
print(encode('ABCDE'))