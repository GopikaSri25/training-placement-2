class Solution {
    public int minMaxGame(int[] nums) {
       int gap=1;
       int p=nums[0];
       while(gap<nums.length){
       boolean isMin=true;
       for(int i=0;i+gap<nums.length;i+=gap*2){
            if(isMin){
                nums[i]=Math.min(nums[i],nums[i+gap]);
                p=nums[i];
            }
            else{
                nums[i]=Math.max(nums[i],nums[i+gap]);
                p=nums[i];
            }
            isMin=!isMin;
        }
        gap*=2;
    }
    return p;

    }
}
