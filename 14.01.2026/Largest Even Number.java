class Solution {
    public String largestEven(String s) {
        char[] arr=s.toCharArray();
        for(int i=s.length()-1; i>=0; i--){
            if(arr[i]=='2'){
                return s.substring(0,i+1);
            }
        }
        return "";
    }
}
