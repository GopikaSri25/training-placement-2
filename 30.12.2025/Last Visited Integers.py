class Solution(object):
    def lastVisitedIntegers(self, nums):
        seen = []
        ans = []
        maxi = 0

        for num in nums:
            if num != -1:
                seen.insert(0, num)
                maxi = 0
            else:
                maxi += 1
                if maxi <= len(seen):
                    ans.append(seen[maxi - 1])
                else:
                    ans.append(-1)

        return ans
