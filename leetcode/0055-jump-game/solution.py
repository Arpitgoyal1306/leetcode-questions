# Runtime: 10 ms
# Memory: 13 MB

class Solution(object):
    def canJump(self, nums):
        count = 0
        for i in nums:
            if count < 0:
                return False
            elif i > count:
                count = i
            count -= 1
        return True