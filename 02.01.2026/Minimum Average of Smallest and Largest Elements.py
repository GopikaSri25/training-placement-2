class Solution(object):
    def minimumAverage(self, nums):
        r = sorted(nums)
        k = len(nums)
        minx = float('inf')
        minx = (r[0] + r[k-1]) / 2.0
        left = 1
        right = k - 2

        while left < right:
            if (r[left] + r[right]) / 2.0 < minx:
                newmin = (r[left] + r[right]) / 2.0
                minx = newmin
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1

        return minx

        
