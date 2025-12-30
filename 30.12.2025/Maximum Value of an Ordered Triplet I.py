class Solution(object):
    def maximumTripletValue(self, nums):
        if len(nums)<3:
            return 0
        max_value =0
        for j in range(1, len(nums)-1):
            max_i= max(nums[:j])
            max_k= max(nums[j+1:])
            max_value= max(max_value, (max_i - nums[j])*max_k)
        return max_value 
