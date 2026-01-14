class Solution {
    public static int facto(int n,int j){
        int p=1;
        for(int i=n; i>=10-j; i--){
            p=p*i;
        }
        return p;
    }
    public int countNumbersWithUniqueDigits(int n) {
        if(n==0){
            return 1;
        }
        if(n==1){
            return 10;
        }
        if(n==2){
            return 91;
        }
        return countNumbersWithUniqueDigits(n-1)+9*facto(9,n-1);
    }
}
