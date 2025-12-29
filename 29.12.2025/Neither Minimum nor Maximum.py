class Solution(object):
    def findNonMinOrMax(self, nums):
        nums.sort()
        if(len(nums)<3):
            return -1
        else:
            return nums[1]
        
