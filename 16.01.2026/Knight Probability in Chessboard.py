class Solution(object):
    def knightProbability(self, n, k, row, column):
        memo={}
        def dfs(i,j,kk):
            if (0>i) or (0>j) or (i>=n) or (j>=n):
                return 0
            if kk==0:
                return 1
            if (i,j,kk) in memo:
                return memo[(i,j,kk)]
            cur=0
            for di,dj in [(-2,-1),(2,-1),(-2,1),(2,1),(1,2),(-1,2),(-1,-2),(1,-2)]:
                cur+=0.125*dfs(i+di,j+dj,kk-1)
            memo[(i,j,kk)]=cur
            memo[(n-1-i,j,kk)]=cur
            memo[(i,n-1-j,kk)]=cur
            memo[(n-1-i,n-1-j,kk)]=cur
            return cur

        return dfs(row,column,k)
        
