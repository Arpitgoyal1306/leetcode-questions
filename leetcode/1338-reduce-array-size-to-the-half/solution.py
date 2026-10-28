# Runtime: 52 ms
# Memory: 23.2 MB

from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        # for ele,f in Counter(arr).most_common()
        d = {}
        for x in arr:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        temp = sorted(d.values(),reverse=True)
        removed = 0
        ans = 0
        for f in temp:
            removed += f
            ans += 1
            if removed >= len(arr)/2:
                break
        return ans