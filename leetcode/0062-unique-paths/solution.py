# Runtime: 0 ms
# Memory: 19.1 MB

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)