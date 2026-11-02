# Runtime: 2 ms
# Memory: 12.3 MB

class Solution(object):
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]
        def f(i,j):
            if (i,j) == (m-1,n-1):
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            ways = 0
            if i+1 < m: 
                ways += f(i+1,j) 
            if j+1 < n:
                ways += f(i,j+1)
            memo[i][j] = ways
            return ways
        return f(0,0)
        