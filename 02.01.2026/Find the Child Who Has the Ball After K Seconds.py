class Solution(object):
    def numberOfChild(self, n, k):
        index = 0
        neg = 1
        while (k > 0):
            index += (1 * neg)
            if index == (n - 1) or index == 0:
                neg *= -1
            k -= 1
        return index
