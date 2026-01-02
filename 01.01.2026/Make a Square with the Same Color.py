class Solution(object):
    def canMakeSquare(self, grid):
        for r in range(2):
            for c in range(2): 
                x = [i for i in grid[r][c]+grid[r][c+1]+grid[r+1][c]+grid[r+1][c+1]]
                if x.count('B') == 3 or x.count('B') == 4 or x.count('W') == 3 or x.count('W') == 4:
                    return True
        return False
