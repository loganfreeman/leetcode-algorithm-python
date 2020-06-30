class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = dict()
        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            for r in self.dfs(s[len(word):], wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res

sol = Solution()

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(sol.wordBreak(s, wordDict))