class Solution {
    public boolean isTrionic(int[] nums) {
         boolean p = false, q = false, n = false;
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > prev && !q && !n) {
                prev = nums[i];
                p = true;
            } else if (nums[i] < prev && p && !n) {
                prev = nums[i];
                q = true;
            } else if (nums[i] > prev && q) {
                prev = nums[i];
                n = true;
            } else {
                return false;
            }
        }
        return p && q && n;
    }
}
