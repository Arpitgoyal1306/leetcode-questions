# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def uniqueOccurrences(self, arr):
        from collections import Counter

        freq = Counter(arr)
        if len(set(freq.values())) != len(freq):
            return False
        return True
