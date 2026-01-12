class Solution {
    public int[] transformArray(int[] nums) {
        int[]ans=new int[nums.length];
        int index=0;
        for(int i=0;i< nums.length;i++){
            if(nums[i]%2==0){
               ans[index++]=0;
            }else{
                ans[index++]=1;
            }
        }
        Arrays.sort(ans);
        return ans;
    }
}
