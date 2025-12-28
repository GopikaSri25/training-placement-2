class Solution(object):
    def maximizeSum(self, nums, k):
        c = max(nums)*k 
        for i in range(1,k):
            c += i
        return c


        
