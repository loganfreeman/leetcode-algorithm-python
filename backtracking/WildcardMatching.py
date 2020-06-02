class Solution(object):
    """
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
    """

    def isMatch(self, s, p):
        """
Let’s consider any character in the pattern.

Case 1: The character is ‘*’
Here two cases arise

We can ignore ‘*’ character and move to next character in the Pattern.
‘*’ character matches with one or more characters in Text. Here we will move to next character in the string.
Case 2: The character is ‘?’
We can ignore current character in Text and move to next character in the Pattern and Text.

Case 3: The character is not a wildcard character
If current character in Text matches with current character in Pattern, we move to next character in the Pattern and Text. If they do not match, wildcard pattern and Text do not match.

We can use Dynamic Programming to solve this problem –
Let T[i][j] is true if first i characters in given string matches the first j characters of pattern.

DP initilization:

// both text and pattern are null
T[0][0] = true;

// pattern is null
T[i][0] = false;

// text is null
T[0][j] = T[0][j - 1] if pattern[j – 1] is '*'

DP relation:
// If current characters match, result is same as
// result for lengths minus one. Characters match
// in two cases:
// a) If pattern character is '?' then it matches
//    with any character of text.
// b) If current characters in both match
if ( pattern[j – 1] == ‘?’) ||
     (pattern[j – 1] == text[i - 1])
    T[i][j] = T[i-1][j-1]

// If we encounter ‘*’, two choices are possible-
// a) We ignore ‘*’ character and move to next
//    character in the pattern, i.e., ‘*’
//    indicates an empty sequence.
// b) '*' character matches with ith character in
//     input
else if (pattern[j – 1] == ‘*’)
    T[i][j] = T[i][j-1] || T[i-1][j]

else // if (pattern[j – 1] != text[i - 1])
    T[i][j]  = false
        """
        n = len(s)
        m = len(p)
        if (m == 0):
            return (n == 0)

        lookup = [[False for i in range(m+1)] for j in range(n+1)]

        lookup[0][0] = True

        for j in range(1, m+1):
            if (p[j-1] == '*'):
                lookup[0][j] = lookup[0][j-1]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if (p[j-1] == '*'):
                    lookup[i][j] = lookup[i][j-1] or lookup[i-1][j]
                elif (p[j-1] == '?' or s[i-1] == p[j-1]):
                    lookup[i][j] = lookup[i-1][j-1]
                else:
                    lookup[i][j] = False

        return lookup[n][m]


strr = "baaabab"
pattern = "*****ba*****ab"
# char pattern[] = "ba*****ab"
# char pattern[] = "ba*ab"
# char pattern[] = "a*ab"
# char pattern[] = "a*****ab"
# char pattern[] = "*a*****ab"
# char pattern[] = "ba*ab****"
# char pattern[] = "****"
# char pattern[] = "*"
# char pattern[] = "aa?ab"
# char pattern[] = "b*b"
# char pattern[] = "a*a"
# char pattern[] = "baaabab"
# char pattern[] = "?baaabab"
# char pattern[] = "*baaaba*"
ob1 = Solution()
if (ob1.isMatch(strr, pattern)):
    print("Yes")
else:
    print("No")
