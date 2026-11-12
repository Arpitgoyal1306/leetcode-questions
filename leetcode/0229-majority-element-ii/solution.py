# Runtime: 28 ms
# Memory: 19.5 MB

class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        res = Counter(nums)
        abc = res.most_common()
        bac = []
        for i,j in abc:
            if j > (len(nums)//3):
                bac.append(i)
        return bac