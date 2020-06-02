class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0] * n for i in range(m)]

        if (obstacleGrid[0][0] == 0):
            paths[0][0] = 1

        for i in range(1, m):
            if (obstacleGrid[i][0] == 0):
                paths[i][0] = paths[i-1][0]

        for i in range(1, n):
            if (obstacleGrid[0][i] == 0):
                paths[0][i] = paths[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                if (obstacleGrid[i][j] == 0):
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[-1][-1]


obj = Solution()
A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(obj.uniquePathsWithObstacles(A))
