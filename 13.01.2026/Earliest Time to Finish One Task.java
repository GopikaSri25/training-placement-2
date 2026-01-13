class Solution {
    public int earliestTime(int[][] tasks) {
        int sum ;
        int ans = Integer.MAX_VALUE ;
        for(int i =0 ; i<tasks.length ; i++){
            sum = 0 ;
            for(int j=0 ; j < tasks[i].length ; j++){
                sum += tasks[i][j];
            }
            ans = Math.min(ans , sum) ;
        }
        return ans ;
    }
}
