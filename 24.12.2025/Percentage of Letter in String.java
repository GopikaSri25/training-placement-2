class Solution {
    public int percentageLetter(String s, char l) {
        int len=s.length();
        int c=0;
        for(int i=0;i<len;i++){
            if(s.charAt(i)==l){
              c++;
            }
        }
        
        return (c*100)/len;
    }
}
