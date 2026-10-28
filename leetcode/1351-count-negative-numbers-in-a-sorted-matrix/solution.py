# Runtime: 3 ms
# Memory: 19.9 MB

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count
