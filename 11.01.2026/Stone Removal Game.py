class Solution(object):
    def canAliceWin(self, n):
        a = 10
        b = a - 1
        while n > 0:
            n -= a
            if n < 0:
                return False
            n -= b
            if n < 0:
                return True
            a = b - 1
            b = a - 1
        return False
