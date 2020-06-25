# Recursive implementation of numDecodings
"""This problem is recursive and can be broken in sub-problems. We start from end of the given digit sequence. We initialize the total count of decodings as 0. We recur for two subproblems.
1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add the result to total count.
"""
def numDecodings(s: str) -> int:
    return numDecodingsHelper(s,len(s));

def numDecodingsHelper(s:str, n:int) -> int:
    if n == 0 or n == 1 :
        return 1
    count = 0
    if s[n-1] > "0":
        count = numDecodingsHelper(s,n-1)
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) :
        count += numDecodingsHelper(s, n - 2)
    return count

# Driver program to test above function
digits = "1234"
print("Count is ",numDecodings(digits))

def countDecodingDP(digits, n):

    count = [0] * (n + 1); # A table to store
                           # results of subproblems
    count[0] = 1;
    count[1] = 1;

    for i in range(2, n + 1):

        count[i] = 0;

        # If the last digit is not 0, then last
        # digit must add to the number of words
        if (digits[i - 1] > '0'):
            count[i] = count[i - 1];

        # If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
        if (digits[i - 2] == '1' or
           (digits[i - 2] == '2' and
            digits[i - 1] < '7') ):
            count[i] += count[i - 2];

    return count[n];

