class Solution(object):
    def maxDistance(self, arrays):
        n=len(arrays)
        res=0
        mini=arrays[0][0]
        maxi=arrays[0][-1]
        for i in range(1,n):
            res=max(res,max(abs(maxi-arrays[i][0]),abs(mini-arrays[i][-1])))
            mini=min(mini,arrays[i][0])
            maxi=max(maxi,arrays[i][-1])
        return res

        
