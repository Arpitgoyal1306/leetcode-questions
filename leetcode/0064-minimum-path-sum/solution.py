# Runtime: 39 ms
# Memory: 16 MB

class Solution(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[-1]*m for _ in range(n)]
        def f(i,j):
            if i >= n or j >= m:
                return float('inf')
            if i == n-1 and j == m-1:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            right = f(i,j+1)
            down = f(i+1,j)
            dp[i][j] = grid[i][j] + min(right,down)
            return dp[i][j]
        return f(0,0)
        