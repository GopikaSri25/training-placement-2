class Solution(object):
    def findChampion(self, grid):
        n = len(grid)
        for j in range(n):  
            for i in range(n):  
                if grid[i][j] == 1:  
                    break
            else:
                return j  
