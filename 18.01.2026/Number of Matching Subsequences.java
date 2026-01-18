class Solution {
    public boolean isSubsequence(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        int j=0,i=0;
        while(i<m){
            if(j>=n) return true;
            if(s1.charAt(i)==s2.charAt(j)){
                i++;
                j++;
            }
            else i++;
        }
        if(j>=n) return true;
        return false;
    }
    public int numMatchingSubseq(String s1, String[] words) {
        int count = 0;
        HashMap<String, Integer> map = new HashMap<>();
        for (String w : words) map.put(w, map.getOrDefault(w, 0) + 1);

        for(String s2 : map.keySet()){
            if(isSubsequence(s1,s2)) count+=map.get(s2);
        }
        return count;
    }
}
