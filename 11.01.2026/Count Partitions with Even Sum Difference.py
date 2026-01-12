class Solution(object):
    def countPartitions(self, nums):
        count = 0
        for i in range(1, len(nums)):
            left = nums[0:i]
            right = nums[i:]

            if (sum(left) - sum(right)) % 2 == 0:
                count += 1 
        return count
