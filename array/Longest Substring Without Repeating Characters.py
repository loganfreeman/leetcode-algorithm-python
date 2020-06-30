class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setc = set()
        ans = 0
        pre = 0
        for i in range(len(s)):
            if s[i] not in setc:
                setc.add(s[i])
                ans = max(ans, len(setc))
            else:
                while(pre < i):
                    if s[pre] == s[i]:
                        pre += 1
                        break
                    else:
                        setc.remove(s[pre])
                        pre += 1
        return ans
