class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        boolean[] present = new boolean[101];
        int n = nums.length;
        int min = nums[0];
        int max = nums[0];

        for (int x : nums) {
            if (x < min) min = x;
            else if (x > max) max = x;
            present[x] = true;
        }

        List<Integer> ans = new ArrayList<>();
        for (int v = min; v <= max; v++) {
            if (!present[v]) {
                ans.add(v);
            }
        }

        return ans;
    }
}
