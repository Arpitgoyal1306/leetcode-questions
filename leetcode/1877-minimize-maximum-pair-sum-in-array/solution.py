# Runtime: 1084 ms
# Memory: 24.8 MB

class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        j = n - 1
        res = 0
        while i <= j:
            res = max(res,nums[i]+nums[j])
            i+= 1
            j-= 1
        return res