class Solution {
    public int maximumValue(String[] strs) {
        int max=0;
        for(String s:strs){
            boolean flag=true;
            for(char c:s.toCharArray()){
                if(!Character.isDigit(c)){
                    flag=false;
                    break;
                }
            }
            int val;
            if(flag){
                val=Integer.parseInt(s);
            }else{
                val=s.length();
            }
            max=Math.max(val,max);
        }   
        return max;
    }
}
