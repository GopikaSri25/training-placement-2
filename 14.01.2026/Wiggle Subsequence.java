class Solution {
    public int wiggleMaxLength(int[] nums) {
        int n = nums.length;
        int ans = 1;
        if (n==1) return ans;
        int i = 1;
        while (i<n && nums[i]==nums[i-1]) i++;
        if (i==n) return 1;
        boolean flag = nums[i]>nums[i-1];
        for (i = 1; i<n; ) {
            while (i<n && flag && nums[i]>=nums[i-1]) i++;
            while (i<n && !flag && nums[i]<=nums[i-1]) i++;
            flag = !flag;
            ans++;
        }
        return ans;
    }
}
