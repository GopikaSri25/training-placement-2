class Solution(object):
    def returnToBoundaryCount(self, nums):
        d=0
        a=[]
        c=0
        for i in nums :
            d=d+i
            if d==0:
                c+=1
           
        return c
