class Solution(object):
    def isFascinating(self, a):
        b = str(2 * a)
        c = str(3 * a)
        d = str(a) + b + c

        for digit in '123456789':
            if d.count(digit) != 1:
                return False
        return True
