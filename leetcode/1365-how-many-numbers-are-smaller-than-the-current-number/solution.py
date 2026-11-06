# Runtime: 276 ms
# Memory: 12.3 MB

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans