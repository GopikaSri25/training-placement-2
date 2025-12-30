class Solution(object):
    def maximumStrongPairXor(self, nums):
        nums.sort()
        min1=0
        l=0

        for r in range(len(nums)):

            while nums[r]-nums[l]>nums[l]:
                l+=1
            for i in range(l,r):
                min1=max(min1,nums[i]^nums[r])
        return min1

            



        
