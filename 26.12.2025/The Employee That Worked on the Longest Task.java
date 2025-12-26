class Solution {
    public int hardestWorker(int n, int[][] logs) {
        int m = logs.length, prev_val = 0, max_val = 0, res = -1;

        for (int i = 0; i < m; i++){
            if (logs[i][1] - prev_val > max_val){
                max_val = logs[i][1] - prev_val;
                res = logs[i][0];
            } 

            if (logs[i][1] - prev_val == max_val){
                res = Math.min(res,logs[i][0]);
            }

            prev_val = logs[i][1];
        }

        return res;
    }
}
