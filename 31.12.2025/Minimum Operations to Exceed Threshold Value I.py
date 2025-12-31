class Solution(object):
    def minOperations(self, nums, k):
        return sum(1 for x in nums if x < k)
