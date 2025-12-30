class Solution(object):
    def findKOr(self, nums, k):
        bitPosition = [0] * 32

        for i in range(0, len(nums)):
            index = 0
            while (nums[i] != 0):
                bitPosition[index] += nums[i] % 2
                nums[i] /= 2
                index += 1

        result = 0
        for i in range(0, 32): 
            if (bitPosition[i] >= k):
                result += 2 ** i

        return result
