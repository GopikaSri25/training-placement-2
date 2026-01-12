class Solution(object):
    def minOperations(self, nums, k):
        nums_set=set(nums)

        if min(nums_set)<k:
            return -1
        
        operations=0
        for num in nums_set:
            if num>k:
                operations+=1
        return operations
