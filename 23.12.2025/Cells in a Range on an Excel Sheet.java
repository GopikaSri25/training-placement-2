class Solution {
    public List<String> cellsInRange(String s) {
        List<String> result = new ArrayList<>();

        for (int i = s.charAt(1)-'0'; i <= s.charAt(4)-'0'; i++){
            for (char c = s.charAt(0); c <= s.charAt(3); c++){
                result.add(c + "" + i);
            }
        }

        Collections.sort(result);

        return result;
    }
}
