class Solution {
    public String bestHand(int[] ranks, char[] suits) { 

        boolean flush = true;
        for (int i = 1; i < suits.length; i++) {
            if (suits[i] != suits[0]) {
                flush = false;
                break;
            }
        }
        if (flush) return "Flush";

        int[] freq = new int[14]; 
        for (int r : ranks) {
            freq[r]++;
        }

        boolean pair = false;

        for (int count : freq) {
            if (count >= 3) return "Three of a Kind";
            if (count == 2) pair = true;
        }

        if (pair) return "Pair";
        return "High Card";
    }
}
