class Solution {
    public int deleteGreatestValue(int[][] grid) {
        int sum = 0, transpose[][] = new int[grid[0].length][grid.length];
        for(int i=0;i<grid.length;i++) Arrays.sort(grid[i]);
        for(int i=0;i<grid.length;i++)for(int j=0;j<grid[0].length;j++)transpose[j][i] = grid[i][j];
        for(int i=0;i<transpose.length;i++) sum += Arrays.stream(transpose[i]).max().getAsInt();
        return sum;
    }
}
