class Solution(object):
    def duplicateNumbersXOR(self, nums):
        res = {}
        count = 0
        for num in nums:
            res[num] = res.get(num, 0) + 1
            if res[num] == 2:
                count ^= num
        
        return count
        
