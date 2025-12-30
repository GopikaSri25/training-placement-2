class Solution(object):
    def minimumRightShifts(self, nums):
        if nums==sorted(nums):
            return 0
        iteration=len(nums)
        i=0
        while(i<iteration-1):
            ele=nums[-1]
            for j in range(iteration-2,-1,-1):
                nums[j+1]=nums[j]
            i+=1
            nums[0]=ele
            if nums==sorted(nums):
                return i
        return -1

        
