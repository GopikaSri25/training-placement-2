class Solution {
    public int minimumMoves(String s) {
        StringBuilder sb = new StringBuilder(s);
        int moves = 0;
        int index = sb.indexOf("X");
        while(index!=-1){
            moves++;
            for(int i=index; i<index+3; i++){
                sb.setCharAt(i, '0');
                if(i+1==s.length()) return moves;
            }
            index = sb.indexOf("X");
        }
        return moves;
    }
}
