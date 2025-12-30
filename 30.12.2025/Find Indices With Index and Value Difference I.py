class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1,-1]
        
