class Solution(object):
    def findNumberOfLIS(self, nums):
        dp = []

        for n in nums:
            if not dp:
                dp.append([(n, 1)])
            else:
                l, r = 0, len(dp)
                while l < r:
                    m = (r - l) / 2 + l
                    if dp[m][-1][0] < n:
                        l = m + 1
                    else:
                        r = m

                cur_count = sum(l[1] for l in dp[l - 1] if n > l[0]) if l > 0 else 1
                if l < len(dp):
                    dp[l].append((n, cur_count))
                else:
                    dp.append([(n, cur_count)])
        
        return sum([x[1] for x in dp[-1]])
