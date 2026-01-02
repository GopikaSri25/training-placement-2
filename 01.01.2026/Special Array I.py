class Solution(object):
    def isArraySpecial(self, nums):
        if nums[0] % 2 == 0:
            temp = "even"
        else:
            temp = "odd"
        if len(nums) == 1:
            return True
        else:
            for i in range(1,len(nums)):
                if nums[i] % 2 == 0:
                    temp1 = "even"
                else:
                    temp1 = "odd"
                if temp == temp1:
                    return False
                temp = temp1
        return True
