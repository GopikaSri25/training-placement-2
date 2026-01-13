class Solution {
    public int alternatingSum(int[] nums) {
        int n = nums.length;
        int sumE = 0;
        int sumO = 0;
        for(int i=0;i<n;i++){
            if(i%2==0){
                sumE += nums[i];
            }else{
                sumO += nums[i];
            }
        }
        int finalSum = sumE - sumO;
        return finalSum;
    }
}
