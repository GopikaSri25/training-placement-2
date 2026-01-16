import math

class Solution(object):
    def repeatedStringMatch(self, a, b):
        r = int(math.ceil(float(len(b)) / len(a)))
        if b in a * r:
            return r
        elif b in a * (r + 1):
            return r + 1
        else:
            return -1
