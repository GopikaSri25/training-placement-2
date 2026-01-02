class Solution(object):
    def minBitwiseArray(self, nums):
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            n = nums[i]
            cnt = 0
            while n != 0:
                cnt += 1
                n = n >> 1
            n = 2**(cnt-1)-2
            while n < nums[i]:
                if n | n+1 == nums[i]:
                    ans[i] = n
                    break
                n+=1
        return ans
        
