class Solution {
    public String majorityFrequencyGroup(String s) {
        HashMap<Character, Integer> count = new HashMap();
        for(char c : s.toCharArray()) {
                if(count.containsKey(c))
                    count.put(c, count.get(c) +1);
                else
                    count.put(c, 1);
        }
        int [] freq = new int [101];
        for(Character key : count.keySet()) {
            freq[count.get(key)]++;
        }
        int index = 0, max = 0;
        for(int i = 0; i < 101; i++) {
            if(freq[i] >= max) {
                max = freq[i];
                index = i;
            }
        }
        String str = "";
        for(Character key : count.keySet()) {
            if(count.get(key) == index) {
                str += key;
            }
        }
        return str;
    }
}
