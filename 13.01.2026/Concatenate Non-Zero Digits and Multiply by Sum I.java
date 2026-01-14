class Solution {
    public long sumAndMultiply(int n) {
        String num = "";
        long sum = 0;
        String s = Integer.toString(n);
        for(char c : s.toCharArray()){
            if(c == '0'){
                continue;
            }else{
                num += c;
            }
        }
    
        for(char c : num.toCharArray()){
            sum += c - 48; 
        }
        if(num.length() == 0){
            return 0;
        }
        return Long.parseLong(num) * sum;
    }
}
