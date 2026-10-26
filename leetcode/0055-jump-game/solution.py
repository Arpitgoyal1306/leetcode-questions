# Runtime: 19 ms
# Memory: 12.8 MB

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


        # curr = 0
        # for i in range(len(nums)):
        #     if i > curr:
        #         return False
        #     curr = max(curr,i+nums[i])
        # return True
