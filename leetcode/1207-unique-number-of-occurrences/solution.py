# Runtime: 1 ms
# Memory: 12.3 MB

class Solution(object):
    def uniqueOccurrences(self, arr):
        from collections import Counter

        freq = Counter(arr)

        if len(set(freq.values())) != len(freq):
            return False
        return True
