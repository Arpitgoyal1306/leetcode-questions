# Runtime: 32 ms
# Memory: 12.4 MB

class Solution(object):
    def commonChars(self, words):
        from collections import Counter
        common = Counter(words[0])
        for i in range(1, len(words)):
            common = common & Counter(words[i])
        return list(common.elements())