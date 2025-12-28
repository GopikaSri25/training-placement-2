class Solution(object):
    def findTheArrayConcVal(self, nums):
        conc_nums = 0

        while len(nums) > 0:
            if len(nums) == 1:
                conc_nums += nums[0]
                nums.pop(0)
            else:
                conc_str = str(nums[0]) + str(nums[-1])
                nums.pop()
                nums.pop(0)
                conc_nums += int(conc_str)
        
        return conc_nums
