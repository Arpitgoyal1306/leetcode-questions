# Runtime: 26 ms
# Memory: 12.3 MB

class Solution(object):
    def findTheDifference(self, s, t):
        temp = list(s)
        for ch in t:
            if ch in temp:
                temp.remove(ch)
            else:
                return ch