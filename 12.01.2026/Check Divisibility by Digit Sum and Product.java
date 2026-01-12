class Solution {
    public boolean checkDivisibility(int n) {
        int sum=0,pro=1,b=n;
        while(n!=0){
            int t=n%10;
            sum+=t;
            pro*=t;
            n/=10;
        }
        return (b%(sum+pro))==0;
    }
}
