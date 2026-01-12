class Solution:
    def countValidSelections(self, nums):
        total_sum = sum(nums)
        rev_sum = 0
        ans = 0

        if total_sum == 0:
            return len(nums) * 2
        if total_sum == 1:
            return len(nums) - 1

        for i in range(len(nums) - 1, 0, -1):
            total_sum -= nums[i]
            rev_sum += nums[i]

            if nums[i - 1] == 0:
                if total_sum == rev_sum:
                    ans += 2
                elif abs(total_sum - rev_sum) == 1:
                    ans += 1

        return ans
