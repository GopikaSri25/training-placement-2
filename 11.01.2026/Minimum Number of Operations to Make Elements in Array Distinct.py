class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        while len(nums) > 0:
            if len(nums) == len(set(nums)):
                return count
            nums = nums[3:]
            count += 1
        return count
        
