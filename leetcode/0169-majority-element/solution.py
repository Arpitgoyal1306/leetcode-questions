# Runtime: 39 ms
# Memory: 13.6 MB

class Solution(object):
    from collections import Counter
    def majorityElement(self, nums):
        # Method 1

        res = Counter(nums)
        abc = res.most_common()
        if abc > (len(nums)/2):
            return abc[0][0]



        # Method 2

        # candidate = None
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate