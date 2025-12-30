class Solution(object):
    def isGood(self, nums):
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] - nums[i] == 1:
                count +=1
        if nums[0] == 1 and count == n-2 and nums[n-1] == nums[n-2]:
            return True
        return False 
