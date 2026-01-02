class Solution(object):
    def canAliceWin(self, nums):
        single_digit=0
        double_digit=0
        for i in range(len(nums)):
            if len(str(nums[i]))==1:
                single_digit+=nums[i]
            else:
                double_digit+=nums[i]
        return single_digit>double_digit or double_digit>single_digit
sol=Solution()
print(sol.canAliceWin([1,2,3,4,10]))
print(sol.canAliceWin([1,2,3,4,5,14]))
print(sol.canAliceWin([5,5,5,25]))
        
