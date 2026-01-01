class Solution(object):
    def numberGame(self, nums):
        arr = []
        i = len(nums)
        while i > 0:
            minimum1 = min(nums)
            nums.remove(minimum1)
            minimum2 = min(nums)
            nums.remove(minimum2)
            i -= 2
            arr.append(minimum2)
            arr.append(minimum1)
        return arr
        
