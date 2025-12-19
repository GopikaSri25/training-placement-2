class Solution {
    public boolean isPrefixString(String s, String[] words) {
        String t = "";

        for (int i = 0; i < words.length; i++){
            t += words[i];

            if (s.equals(t)){
                return true;
            }
        }

        return false;
    }
}
