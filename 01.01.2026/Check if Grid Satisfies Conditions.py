class Solution(object):
    def satisfiesConditions(self, grid):
        i=0
        while i<len(grid[0])-1:
            if grid[0][i]==grid[0][i+1]:
                return False
            i=i+1
        i=0
        while i<len(grid[0]):
            j=0
            while j<len(grid)-1:
                if grid[j][i]!=grid[j+1][i]:
                    return False
                j=j+1
            i=i+1
            
        return True
