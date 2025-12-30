class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        a=0
        for x in range(len(nums)):
            if bin(x)[2:].count("1")==k:
                a=a+nums[x]
        return a
        
