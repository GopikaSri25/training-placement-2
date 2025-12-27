class Solution(object):
    def maximumCount(self, nums):
        neg=[]
        pos=[]
        zero=[]
        for i in nums:
            if i<0:
                neg.append(i)
            elif i==0:
                zero.append(i)
            else:
                pos.append(i)
        return max(len(neg), len(pos))
