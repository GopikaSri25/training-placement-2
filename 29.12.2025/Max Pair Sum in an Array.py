class Solution(object):
    def maxSum(self, nums):
        largest_digits = []
        for num in nums:
            largest_digits.append(max(
                math.floor(num / 10000),
                (math.floor(num / 1000) % 10),
                (math.floor(num / 100) % 10),
                (math.floor(num / 10) % 10),
                num % 10
            ))

        max_sum = -1
        for i in range(len(largest_digits) - 1):
            for j in range(i + 1, len(largest_digits)):
                if largest_digits[i] == largest_digits[j]:
                    max_sum = max(max_sum, nums[i] + nums[j])

        return max_sum

