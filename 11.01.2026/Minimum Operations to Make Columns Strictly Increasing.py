class Solution(object):
    def minimumOperations(self, grid):
        ans = 0
        for i,v in enumerate(zip(*grid)):
            x=v[0]
            for j in range(1,len(v)):
                if v[j]-x<=0:
                    ans+=(x-v[j]+1)
                    x=x+1
                else:
                    x=v[j]
        return ans
