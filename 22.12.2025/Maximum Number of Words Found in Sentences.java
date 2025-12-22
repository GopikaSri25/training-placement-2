class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = Integer.MIN_VALUE;
        for(String sent : sentences){
            int count =0;
            for(int i=0;i<sent.length();i++){
                if(sent.charAt(i)==' '){
                    count++;
                }
                if(count>max) max = count;
            }
        }
        return max+1;
    }
}
