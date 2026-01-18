class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
            
        lp = 0
        product = 1
        res = 0

        for rp in range(len(nums)):
            product *= nums[rp]

            while product >= k:
                product //= nums[lp]
                lp += 1

            res += rp - lp + 1

        return res
        
