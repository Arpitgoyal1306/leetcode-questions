# Runtime: 2 ms
# Memory: 14.9 MB

class Solution(object):
    def lemonadeChange(self, bills):
        five_dollar = 0
        ten_dollor = 0
        for i in bills:
            if i == 5:
                five_dollar += 1
            elif i == 10:
                if five_dollar >= 1:
                    five_dollar -= 1
                    ten_dollor += 1
                else:
                    return False
            else:
                if five_dollar > 0 and ten_dollor > 0:
                    five_dollar -= 1
                    ten_dollor -= 1
                elif five_dollar >= 3:
                    five_dollar -= 3
                else:
                    return False
        return True
