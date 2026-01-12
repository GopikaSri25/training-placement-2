class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(10):
            num = n + i
            product = 1
            temp = num
            while temp:
                product *= temp % 10
                temp //= 10
            if product % t == 0:
                return num

        
