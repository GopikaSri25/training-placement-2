class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) continue; 

            int slow = i;
            int fast = i;
            boolean forward = nums[i] > 0;

            while (true) {
                slow = next(nums, slow, forward);
                if (slow == -1) break;

                fast = next(nums, fast, forward);
                if (fast == -1) break;

                fast = next(nums, fast, forward);
                if (fast == -1) break;

                if (slow == fast) {
        
                    if (slow == next(nums, slow, forward)) break;
                    return true;
                }
            }
            int idx = i;
            while (nums[idx] != 0 && (nums[idx] > 0) == forward) {
                int next = ((idx + nums[idx]) % n + n) % n;
                nums[idx] = 0;
                idx = next;
            }
        }
        return false;
    }

    private int next(int[] nums, int i, boolean forward) {
        if ((nums[i] > 0) != forward) return -1;

        int n = nums.length;
        int next = ((i + nums[i]) % n + n) % n;

        if (next == i) return -1; 
        return next;
    }
}
