
class Solution(object):
    def partitionLabels(self, s):
        last_index={}
        end=0
        size=0
        res=[]
        for i,c in enumerate(s):
            last_index[c]=i
        for i,c in enumerate(s):
            end=max(end,last_index[c])
            size+=1
            if i==end:
                res.append(size)
                size=0
        return res
