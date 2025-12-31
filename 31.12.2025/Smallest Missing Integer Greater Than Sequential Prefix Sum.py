class Solution(object):
    def missingInteger(self, nums):
        left = 0
        right =len(nums) - 1
        sum_num = nums[0]
        out = 0
        while left < right:
            temp = nums[left]
            if temp+1 == nums[left+1]:
                sum_num = sum_num + nums[left+1]
                left+=1
            else:
                out=left
                break;

        while sum_num in nums[out:]:
            sum_num+=1
        return sum_num
        
