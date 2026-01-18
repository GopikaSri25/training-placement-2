class Solution(object):
    def findLength(self, nums1, nums2):
        dp = {i-1: 0 for i in range(len(nums1))}
        ans = 0 
        p = 0 
        while p < len(nums2):
            new_dp = {}
            for i in range(len(nums1)):
                if nums1[i] == nums2[p]:
                    if (i-1) in dp:
                        new_dp[i] = dp[i-1] + 1
                    else:
                        new_dp[i] = 1
                    ans = max(ans, new_dp[i])
                        
            dp = new_dp 
            p += 1
        
        return ans
        
        
