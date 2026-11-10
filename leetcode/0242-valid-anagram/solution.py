# Runtime: 27 ms
# Memory: 12.4 MB

class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

        