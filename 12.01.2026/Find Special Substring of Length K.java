class Solution {
    public boolean hasSpecialSubstring(String s, int k) {
        int n = s.length(), count = 1;

        char cur = s.charAt(0);

        for (int i = 1; i < n; i++){
            if (s.charAt(i) == cur){
                count += 1;
            } else {
                if (count == k){
                    return true;
                }
                cur = s.charAt(i);
                count = 1;
            }
        }

        return count == k;
    }
}
