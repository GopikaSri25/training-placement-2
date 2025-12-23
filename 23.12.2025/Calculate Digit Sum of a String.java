import java.math.*;
class Solution {
    public String digitSum(String s, int k) {
        while(s.length()>k){
            StringBuilder word=new StringBuilder();
            int len=s.length();
            if(len%k!=0){
                int mod=len%k;
                len-=mod;
            }
            int i=0;
            while(i<len){
                String b=s.substring(i,i+k);
                word.append(num(b));
                i=i+k;
            }
            if(i!=s.length()){
                StringBuilder sb=new StringBuilder();
                while(i<s.length()){
                    sb.append(s.charAt(i));
                    i++;
                }
                if(sb.length()!=0){
                    word.append(num(sb.toString()));
                }
            }
            s=word.toString();
        }
        return s;
    }
    public static String num(String s){
        int sum=0;
        for(char c:s.toCharArray()){
            int as=(int)c;
            as-=48;
            sum+=as;
        }
        return Integer.toString(sum);
    }
}
