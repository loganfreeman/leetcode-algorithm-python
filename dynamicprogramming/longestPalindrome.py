class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenS = len(s)
        arr = [ [0] * lenS for i in range(lenS)]
        for i in range(lenS):
            arr[i][i] = 1

        res = 0
        for i in range(1, lenS):
            for j in range(i):
                if s[i] == s[j]:
                    if i == j + 1:
                        arr[i][j] = 2
                    else:
                        if arr[i-1][j-1] > 0:
                            arr[i][j] = 2 + arr[i-1][j-1]

                    if arr[i][j] > res:
                        res = arr[i][j]
        return res