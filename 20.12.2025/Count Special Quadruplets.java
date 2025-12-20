class Solution {
    public int countQuadruplets(int[] nums) {
        int ans=0;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                for(int k=j+1;k<nums.length;k++){
                    for(int a=k+1;a<nums.length;a++){
                        if(nums[i]+nums[j]+nums[k]==nums[a]){
                            ans++;
                        }
                    }
                }
            }
        }
        return ans;
    }
}
