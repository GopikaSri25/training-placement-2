class Solution {
    public int maxDistance(int[] colors) {
        int max=0;
        for(int j=colors.length-1;j>0;j--){
            if(colors[0]!=colors[j]){
           max=Math.max(max,j);
            }
        }
        for(int j=0;j<colors.length;j++){
            if(colors[colors.length-1]!=colors[j]){
           max=Math.max(max,(colors.length-1)-j); 
            }
        }
       return max; 
    }
}
