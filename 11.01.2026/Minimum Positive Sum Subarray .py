class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n=len(nums)
        minimum=10000000000000000000
        
        for i in range(l,r+1):
            s=sum(nums[:i])
            j=0
            if s>0 and minimum>s:
                    minimum=s
            while j+i<n:
                s=s-nums[j]
                s=s+nums[j+i]
                if s>0 and minimum>s:
                    minimum=s
                
                j+=1
        if minimum ==10000000000000000000:
            return -1
        else:
            return minimum

        
