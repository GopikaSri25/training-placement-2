import java.util.* ; 
class Solution {
    public boolean checkDistances(String s, int[] distance) {
        Map < Character , Integer > freq= new HashMap<>();
        Map < Character , Integer > m= new HashMap<>();
        for (int i = (int)'a' ; i <= (int)'z' ; i++){
            freq.put((char)i , distance[i-97]);
        }
        
        for (int i = 0 ; i < s.length() ; i++){
            if (m.containsKey(s.charAt(i))){
                if (i - m.get(s.charAt(i))-1 != freq.get(s.charAt(i))){
                    return false ;
                }
            }
            else{
                m.put(s.charAt(i) , i);
            }
        }
        
        return true ;
    }
}
