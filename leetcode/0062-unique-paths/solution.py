# Runtime: 2 ms
# Memory: 12.1 MB

class Solution(object):
    def uniquePaths(self, m, n):
        # memoisation

        # memo = [[-1] * n for _ in range(m)]
        # def f(i,j):
        #     if (i,j) == (m-1,n-1):
        #         return 1
        #     if memo[i][j] != -1:
        #         return memo[i][j]
        #     ways = 0
        #     if i+1 < m: 
        #         ways += f(i+1,j) 
        #     if j+1 < n:
        #         ways += f(i,j+1)
        #     memo[i][j] = ways
        #     return ways
        # return f(0,0)



        # tabulation
        
        dp = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i,j) == (m-1,n-1):
                    dp[i][j] = 1
                else:
                    if i+1 < m:
                        dp[i][j] += dp[i+1][j]
                    if j+1 < n:
                        dp[i][j] += dp[i][j+1]
        return dp[0][0]