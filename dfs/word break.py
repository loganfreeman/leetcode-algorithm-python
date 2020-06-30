class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in xrange(1, len(s) + 1):
            for k in xrange(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True

        return dp.pop()
