class Solution(object):
    def maxAdjacentDistance(self, nums):
        max_diff=0
        n=len(nums)
        for i in range(n-1):
            max_diff=max(max_diff,abs(nums[i]-nums[i+1]))
        max_diff=max(max_diff,abs(nums[n-1]-nums[0]))
        return max_diff
