class Solution(object):
    def alternatingSubarray(self, nums):
        max_ = 0
        order = 1
        left = 0
        right = 1
        while True:
            if nums[right]-nums[right-1] == order:
                right += 1
                order *= -1
            else:
                max_ = max(max_, len(nums[left:right]))
                left += 1
                right = left+1
                order = 1

            if right == len(nums):
                max_ = max(max_, len(nums[left:right]))
                break

        return -1 if max_ == 1 else max_
        
