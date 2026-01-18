class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        int len = nums.length;
        int l=0;
        int r=0;
        int subCount=0;
        int count=0;

        while(r<len){
            if(nums[r]>right){
                subCount=0;
                l=r+1;
            }else if((nums[r]>=left && nums[r]<=right)){
                subCount=r-l+1;
            }
            r++;
            count+=subCount;
        }

        return count;
    }
}
