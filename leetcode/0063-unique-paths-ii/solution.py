# Runtime: 1 ms
# Memory: 12.5 MB

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1]*m for _ in range(n)]
        def f(i,j):
            if i >= n or j >= m:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == n-1 and j == m-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            right = f(i,j+1)
            down = f(i+1,j)
            dp[i][j] = (right + down)
            return dp[i][j]
        return f(0,0)