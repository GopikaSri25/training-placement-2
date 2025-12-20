class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] empty={};
        if(m*n!=original.length)
        return empty;
        int[][] res=new int[m][n];
        int index=0;
        for(int row=0;row<m;row++){
            for(int col=0;col<n;col++){
                res[row][col]=original[index];
                index++;
            }
        }
        return res;
    }
}
