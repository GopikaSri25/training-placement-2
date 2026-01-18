class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0 
        
        max_val = max(nums)
        earn = [0] * (max_val + 1)

        for num in nums:
            earn[num] += num
        
        dp = [0] * (max_val + 1)
        dp[0] = 0 
        dp[1] = earn[1]

        for i in range(2, max_val + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + earn[i])
        
        return dp[max_val]
        
