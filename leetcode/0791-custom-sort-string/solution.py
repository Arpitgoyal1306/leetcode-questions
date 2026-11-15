# Runtime: 0 ms
# Memory: 12.1 MB

class Solution(object):
    def customSortString(self, order, s):
        from collections import Counter
        freq = Counter(s)
        ans = ""
        for ch in order:
            ans += ch * freq[ch]
            freq[ch] = 0
        ans += ''.join(freq.elements())
        return ans