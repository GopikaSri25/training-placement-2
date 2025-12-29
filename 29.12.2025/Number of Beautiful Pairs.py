class Solution(object):
    def countBeautifulPairs(self, nums):
        def check(x , y):
            while y != 0:
                x , y = y , x % y
            return x == 1
        def firstDigit(x):
            while x >= 10:
                x = x // 10
            return x
        def lastDigit(x):
            return x % 10
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                first = firstDigit(num1)
                last = lastDigit(num2)
                if check(first , last):
                    res += 1
        return res 
