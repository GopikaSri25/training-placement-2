class Solution {
    public int minTimeToType(String word) {
        int n = word.length();

        int total = Math.min(26-Math.abs((int)word.charAt(0) - (int)'a'),Math.abs((int)word.charAt(0) - (int)'a'));

        for (int i = 1; i < n; i++){
            total += Math.min(26-Math.abs((int)word.charAt(i) - (int)word.charAt(i-1)),Math.abs((int)word.charAt(i) - (int)word.charAt(i-1)));
        }

        return total + n;
    }
}
