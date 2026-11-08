# Runtime: 0 ms
# Memory: 12.1 MB

class Solution(object):
    def repeatedCharacter(self, s):
        for i in range(len(s)):
            count = 0
            for j in range(i + 1):
                if s[i] == s[j]:
                    count += 1
            if count == 2:
                return s[i]