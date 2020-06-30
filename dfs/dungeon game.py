class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [ [0] * n for i in range(m)]

        dp[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1)

        for i in range(1, n):
            dp[m-1][(n - i - 1)] = max(dp[m-1][n-i] - dungeon[m-1][n-i-1], 1)

        for i in range(1, m):
            dp[m-1-i][(n - 1)] = max(dp[m-i][n-1] - dungeon[m-1-i][n-1], 1)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                down = max(dp[i + 1][j] - dungeon[i][j], 1)
                right = max(dp[i][j + 1] - dungeon[i][j], 1)
                dp[i][j] = min(right, down)
        return dp[0][0]

ob = Solution()
print(ob.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))