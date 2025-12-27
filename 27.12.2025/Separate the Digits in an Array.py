class Solution(object):
    def separateDigits(self, nums):
        res=[]
        for i in nums:
            k=str(i)
            for j in k:
                res.append(int(j))
        return res
