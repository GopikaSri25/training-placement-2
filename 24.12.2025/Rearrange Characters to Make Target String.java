class Solution {
    public int rearrangeCharacters(String strings, String target) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (char s : strings.toCharArray()) {
            if (target.indexOf(s) != -1) {
                map.put(s, map.getOrDefault(s, 0) + 1);
            }
        }
        
        boolean flag = true;
        int count = 0;
        
        while (flag) {
            for (char c : target.toCharArray()) {
                if (!map.containsKey(c)) {
                    flag = false;
                    break;
                }

                int newVal = map.get(c) - 1;

                if (newVal == 0) {
                    map.remove(c);
                } else {
                    map.put(c, newVal);
                }
            }
            
            if (flag) count++;
        }

        return count;
    }
}
