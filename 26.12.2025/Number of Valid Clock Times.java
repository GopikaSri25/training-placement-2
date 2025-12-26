class Solution {
    public int countTime(String time) {
        int output = 1;
        if(time.charAt(0) == '?'){
            char nextChar = time.charAt(1);
            if(nextChar != '?'){
                int next = (int) nextChar - '0';
                if(next >= 4){
                    output *= 2;
                }else{
                    output *= 3;
                }
            }else{
                output *= 24;
            }
            
        }
        if(time.charAt(1) == '?'){
            char prevChar = time.charAt(0);
            if(prevChar != '?'){
                int prev = (int) prevChar - '0';
                if(prev == 2){
                    output *= 4;
                }else{
                    output *= 10;
                }
            }else{
            }
            
        }
        if(time.charAt(3) == '?'){
            output *= 6;
        }
        if(time.charAt(4) == '?'){
            output *= 10;
        }
        return output;
    }
}
