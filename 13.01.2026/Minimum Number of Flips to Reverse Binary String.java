class Solution {
    public int minimumFlips(int n) {
        int ct=0;
        for (int lftMsk=Integer.highestOneBit(n), revShft=31-Integer.numberOfLeadingZeros(n);
                lftMsk > 1;
                n>>=1, lftMsk>>=2, revShft-=2)
            if ((((lftMsk&n)>>revShft) ^ 1&n)!=0)
                ++ct;
        return ct*2;
    }
}
