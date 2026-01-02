class Solution(object):
    def getFinalState(self, nums, k, multiplier):

        while k:
            m = min(nums)              
            i = nums.index(m)          
            nums[i] = m * multiplier   
            k -= 1                     
        return nums
