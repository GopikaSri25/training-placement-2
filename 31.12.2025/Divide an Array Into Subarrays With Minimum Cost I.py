class Solution(object):
    def minimumCost(self, nums):
        if len(nums)==3:
            return sum(nums)
        minimum=nums[0]
        nums.pop(0)
        q=min(nums)
        nums.remove(q)
        return minimum+q+min(nums)
