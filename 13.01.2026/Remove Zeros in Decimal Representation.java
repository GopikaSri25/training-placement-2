class Solution {
    public long removeZeros(long n) {
    long temp = n;
    long num = 0;
    long digits = (long)(Math.log10(n)+1);
    while(digits>=0){
        long digit = (long)(temp/Math.pow(10,digits))%10;
        if(digit>0){
            num = num*10+digit;
        }
        digits--;
    }
    return num;    
    }
}
