class Solution {
    public int[][] largestLocal(int[][] grid) {
        int n = grid.length-2;
        int[][] ans = new int [n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int maxVal = 0;
                for(int k = i; k < i+3; k++){
                    for(int l = j; l < j+3; l++){
                        maxVal = Math.max(maxVal, grid[k][l]);
                    }
                }
                ans[i][j] = maxVal;
            }
        }
        return ans;
    }
}
