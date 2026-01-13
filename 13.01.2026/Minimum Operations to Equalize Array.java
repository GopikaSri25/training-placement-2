class Solution {
    public int minOperations(int[] nums) {
        int ele=nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=ele) return 1;
        }
        return 0;
    }
}
