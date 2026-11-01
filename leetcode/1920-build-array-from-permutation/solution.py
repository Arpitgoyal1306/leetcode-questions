# Runtime: 6 ms
# Memory: 12.6 MB

class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

        