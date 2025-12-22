class Solution {
    public int[] sortEvenOdd(int[] nums) {
        for(int i=0;i<nums.length-2;i+=2)        
            for(int j=0;j<nums.length-2-i;j+=2)
                if(nums[j]>nums[j+2]){
                    int t=nums[j];
                    nums[j]=nums[j+2];
                    nums[j+2]=t;
                }
        for(int i=1;i<nums.length-2;i+=2)        
            for(int j=1;j<=nums.length-2-i;j+=2)
                if(nums[j]<nums[j+2]){
                    int t=nums[j];
                    nums[j]=nums[j+2];
                    nums[j+2]=t;
                }
        return nums;
    }
}
