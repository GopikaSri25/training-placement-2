class Solution {
    public int countVowelSubstrings(String word) {
        int len = word.length();
        int count=0;
        Set<Character> set = new HashSet<>();
        for(int i=0;i<len-4;i++){
            set.clear();
            for(int j=i;j<len;j++){
                char ch = word.charAt(j);
                if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                    set.add(ch);
                    if(set.size()==5){
                        count++;
                    }
                }else{
                    break;
                }
            }
        }
        return count;
    }
}
