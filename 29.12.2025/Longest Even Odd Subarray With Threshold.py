class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        max_len = 0

        for i in range(n):
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue

            length = 1  
            for j in range(i + 1, n):
                if nums[j] > threshold:
                    break

                if nums[j] % 2 == nums[j - 1] % 2:
                    break
                length += 1

            max_len = max(max_len, length)

        return max_len
