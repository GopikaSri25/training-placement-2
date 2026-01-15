class Solution(object):
    def findUnsortedSubarray(self, nums):
        maxI = -1
        minI = len(nums)

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                tmp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = tmp

                maxI = max(i+1,maxI)
                minI = min(i,minI)

        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp

                maxI = max(i,maxI)
                minI = min(i-1,minI)


        if maxI == -1:
            return 0

        return maxI-minI+1


       
