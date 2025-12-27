class Solution(object):
    def differenceOfSum(self, nums):
        element = 0
        digit = 0
        for i in nums:
            element += i
            while i > 0:
                digit += i % 10
                i //= 10
        return abs(element - digit)
        
