class Solution(object):
    def smallestNumber(self, n):
        if n == 0:
            return '0'
        nn = 1
        while n > 0:
            n = n // 2
            nn *=  2
        return nn-1

        
