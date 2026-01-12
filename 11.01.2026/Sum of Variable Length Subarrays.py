class Solution(object):
    def subarraySum(self, nums):
        
        return  sum(sum(nums[max(0,i-nums[i]):i+1]) for i in range(len(nums)) )
