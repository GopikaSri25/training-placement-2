class Solution {
    public int minBitFlips(int start, int goal) {
        int a = start^goal;
        int b = a;
        int count = 0;
        while(b!=0){
            if((b&1)==1){
                count++;
            }
            b=b>>1;
        }
        return count;
    }
}
