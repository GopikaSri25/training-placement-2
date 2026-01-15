class Solution(object):
    def checkPossibility(self, nums):
        c=0
        for idx in range(1,len(nums)):
            if nums[idx-1]>nums[idx]:
                if c==1:
                    return False
                c+=1
                if idx>=2 and nums[idx-2]>nums[idx]:
                    nums[idx]=nums[idx-1]   
        return True
