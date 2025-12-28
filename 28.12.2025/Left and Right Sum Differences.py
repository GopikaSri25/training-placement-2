class Solution(object):
    def leftRightDifference(self, nums):
        length = len(nums)
        leftSum = [0] * length
        rightSum = [0] * length
        newSum = [0] * length

        for i in range(1, length):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

        for j in range(length - 2, -1, -1):
            rightSum[j] = rightSum[j + 1] + nums[j + 1]

        for k in range(length):
            newSum[k] = abs(leftSum[k] - rightSum[k])

        return newSum
