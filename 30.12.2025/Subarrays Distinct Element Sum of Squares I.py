class Solution(object):
    def sumCounts(self, nums):
        a=0
        for x in range(len(nums)):
            b=x+1
            for y in range(0,len(nums)-b+1):
                a=a+pow(len(set(nums[y:y+b])),2)
        return a
