class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int y=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0){
           y=y|nums[i];
            }
        }
        return y;
    }
}
