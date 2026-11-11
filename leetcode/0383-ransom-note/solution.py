# Runtime: 74 ms
# Memory: 12.1 MB

class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        a = Counter(magazine)
        b = Counter(ransomNote)
        for i in b:
            if b[i] > a[i]:
                return False
        return True