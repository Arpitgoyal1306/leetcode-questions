# Runtime: 24 ms
# Memory: 13.4 MB

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        final = []
        for ch,f in Counter(s).most_common():
            final.append(ch*f)
        return "".join(final)
        # dic = {}
        # for ch in s:
        #     if ch in dic:
        #         dic[ch] += 1
        #     else:
        #         dic[ch] = 1
        # arr = []
        # for ch,f in dic.items():
        #     arr.append([f,ch])
        # arr.sort(reverse=True)
        # final = []
        # for f,ch in arr:
        #     final.append(ch*f)
        # return "".join(final)

