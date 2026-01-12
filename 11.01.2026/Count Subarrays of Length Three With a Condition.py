class Solution(object):
    def countSubarrays(self, nums):
        n = len(nums)
        count = 0
        for i in range(n-2):
            if nums[i+1] == (nums[i]+nums[i+2])*2:
                count += 1
        return count

        
