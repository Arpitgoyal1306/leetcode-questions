# Runtime: 13 ms
# Memory: 13.3 MB

class Solution(object):
    from collections import Counter
    def majorityElement(self, nums):
        # res = Counter(nums)
        # abc = res.most_common()
        # if abc > (len(nums)/2):
        #     return abc[0][0]

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate