# Runtime: 25 ms
# Memory: 13.2 MB

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        return "".join([ch *f for ch,f in Counter(s).most_common()])

        # final = []
        # for ch,f in Counter(s).most_common():
        #     final.append(ch*f)
        # return "".join(final)


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

