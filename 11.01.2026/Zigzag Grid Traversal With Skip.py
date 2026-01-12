class Solution(object):
    def zigzagTraversal(self, grid):
        ans = []
        n, m = len(grid), len(grid[0])
        i = 0
        pos = False
        j = 0
        while i < n:
            pos = not pos
            if pos:
                while j < m:
                    ans.append(grid[i][j])
                    j += 2
                if j == m:
                    j = m-1
                else:
                    j = m-2
            else:
                while j>=0:
                    ans.append(grid[i][j])
                    j -= 2
                if j == -1:
                    j = 0
                else:
                    j = 1
            i += 1
        return ans
                 
