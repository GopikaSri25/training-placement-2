class Solution(object):
    def resultArray(self, nums):
        arr1=[]
        arr2=[]
        n1=nums[0]
        arr1.append(n1)
        n2=nums[1]
        arr2.append(n2)
        for i in range(2,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
