class Solution(object):
    def traverse(self,arr,val,indx,flag):
        res = 0
        n = len(arr)
        rem = val % n

        if flag == 0:
            indx = indx + rem
            if indx >=n:
                indx = indx - n 
            return arr[indx]
        else:
            arr = arr[::-1]
            indx = n -1 - indx
            indx = indx + rem
            if indx >=n:
                indx = indx - n 
            return arr[indx]
    def constructTransformedArray(self, nums):
        result = []
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(self.traverse(nums,abs(nums[i]),i,0))
            elif nums[i]<0:
                result.append(self.traverse(nums,abs(nums[i]),i,1))
            else:
                result.append(nums[i])
        return result            
        
