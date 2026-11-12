# Runtime: 39 ms
# Memory: 13.3 MB

class Solution(object):
    from collections import Counter
    def majorityElement(self, nums):
        res = Counter(nums)
        abc = res.most_common()
        if abc > (len(nums)/2):
            return abc[0][0]