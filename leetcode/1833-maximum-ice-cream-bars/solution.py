# Runtime: 120 ms
# Memory: 20.6 MB

class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        sum_count = 0
        for i in costs:
            if i <= coins:
                sum_count += 1
                coins -= i
            else:
                break
        return sum_count