class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        grid = [[1] * n for _ in range(n)]
        
        for mine in mines:
            x, y = mine
            grid[x][y] = 0
        
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
                    up[i][j] = 1 if i == 0 else up[i - 1][j] + 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1 if j == n - 1 else right[i][j + 1] + 1
                    down[i][j] = 1 if i == n - 1 else down[i + 1][j] + 1
        
        max_order = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                    max_order = max(max_order, order)
        
        return max_order
