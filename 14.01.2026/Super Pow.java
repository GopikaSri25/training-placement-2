class Solution {
    private int MOD = 1337;

   
    public int pow(int A, int B, int C) {
        if (A == 1) return 1;
        if (B == 0) return 1;

        long ans = pow(A, B / 2, C);
        ans = (ans * ans) % C;
        if (B % 2 == 1){
            ans = (ans * A) % C;
        } 
        ans = (ans + C) % C;
        return (int)ans;
    }

   
    public int superPow(int a, int[] b) {
        int result = 1;
        for (int i=0;i<b.length;i++) {
            int digit=b[i];
            result = pow(result, 10, MOD);
            result = (result * pow(a, digit, MOD)) % MOD;
        }
        return result;
    }
}
