# Runtime: 2 ms
# Memory: 12.4 MB

class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        for i in sentences:
            count = max(len(i.split()),count)
        return count