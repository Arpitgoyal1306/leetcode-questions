# Runtime: 656 ms
# Memory: 12.5 MB

class Solution(object):
    def findDifference(self, nums1, nums2):
        ans1 = []
        ans2 = []

        for num in nums1:
            if num not in nums2 and num not in ans1:
                ans1.append(num)

        for num in nums2:
            if num not in nums1 and num not in ans2:
                ans2.append(num)

        return [ans1, ans2]