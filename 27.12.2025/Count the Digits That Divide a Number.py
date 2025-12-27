class Solution(object):
    def countDigits(self, num):
        count = 0
        nums = num
        while nums:
            val = nums % 10 
            if val != 0 and num % val == 0:
                count += 1
            nums = nums // 10
        return count
