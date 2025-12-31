class Solution(object):
    def maxOperations(self, nums):
        ops = 0

        score_val = 0

        prev_score = 0

        while True:
            if len(nums) < 2:
                break
            
            score_val = nums[0] + nums[1]

            print(score_val)

            nums.remove(nums[0])
            nums.remove(nums[0])

            if prev_score > 0 and score_val != prev_score:
                break
            
            prev_score = score_val

            ops += 1
            

        return ops
