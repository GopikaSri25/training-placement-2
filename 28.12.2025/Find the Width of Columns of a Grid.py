class Solution(object):
    def findColumnWidth(self, grid):
        rows, cols = len(grid), len(grid[0])
        solution = []
        for col in range(cols):
            max_col = 0
            for row in range(rows):
                value = len(str(grid[row][col]))
                if value > max_col:
                    max_col = value
            solution.append(max_col)
        return solution
