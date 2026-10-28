# Runtime: 288 ms
# Memory: 32.6 MB

import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        # print(heap)
        original_sum = sum(nums)
        curr_sum = original_sum
        operations = 0
        while curr_sum > original_sum/2:
            operations += 1
            maxi = -heapq.heappop(heap)
            curr_sum -= maxi/2
            heapq.heappush(heap,-maxi/2)
        return operations