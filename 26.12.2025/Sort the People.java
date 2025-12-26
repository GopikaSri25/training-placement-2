class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        Map<Integer, String> m = new TreeMap<>((a, b) -> b - a);

        for (int i = 0; i < names.length; i++) {
            m.put(heights[i], names[i]);
        }

        String[] ans = new String[names.length];
        int i = 0;

        for (Map.Entry<Integer, String> e : m.entrySet()) {
            ans[i] = e.getValue();
            i++;
        }

        return ans;
    }
}
