class Solution {
    public boolean equalFrequency(String word) {
        Set<Integer> set = new HashSet<>();
        int[] freq = new int[26];

        for(char c:word.toCharArray()){
            freq[c - 'a']++;
        }


        boolean isPossible = false;

        for(char c:word.toCharArray()){
            freq[c-'a']--;
            
            for(char i=0 ; i < 26 ; i++){
                if(freq[i] == 0) continue;
                set.add(freq[i]);
            }
            if((set.size()==1)){
                return true;
            }
            set.clear();
             freq[c-'a']++;

        }

        return isPossible;

        
    }
}
