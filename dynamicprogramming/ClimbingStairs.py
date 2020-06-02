class Solution(object):
    def climbStaris(self, n):
        """[summary]

  You are climbing a stair case. It takes n steps to reach to the top.

  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

  Note: Given n will be a positive integer.
        """
        if (n <= 1):
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


obj = Solution()
print(obj.climbStaris(10))
