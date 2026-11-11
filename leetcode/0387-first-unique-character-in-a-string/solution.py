# Runtime: 175 ms
# Memory: 15.6 MB

class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        ran = Counter(s)
        for i in range(len(s)):
            if ran[s[i]] == 1:
                return i
        return -1