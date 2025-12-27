class Solution {
    public int[] applyOperations(int[] nums) {
      for(int i=0;i<nums.length-1;i++){
        if(nums[i]==nums[i+1]){
            nums[i]=nums[i]*2;
            nums[i+1]=0;
        }
      }  
      return movezeros(nums);
    }
    private int[] movezeros(int[] arr){
        int[] arr1=new int[arr.length];
        int j=0;
        for(int i=0;i<arr.length;i++){
        if(arr[i]!=0){
            arr1[j++]=arr[i];
        }
        }
        return arr1;
    }
}
