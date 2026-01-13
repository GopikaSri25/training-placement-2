class Solution {
    public int[] maxKDistinct(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        int tacker = 1;
        List<Integer> arr = new ArrayList();
        int lastElement = nums[n-1];
        arr.add(nums[n-1]);
        for(int i =n-2; i>=0; i--){
            if(tacker == k){
                    break;
                }
            if(nums[i]!=lastElement){
                arr.add(nums[i]);
                tacker++;
                lastElement = nums[i]; 
            }
        }
        int [] ans = new int[arr.size()];
        int index = 0;
        for(int j:arr){
            ans[index++]= j;
        }
        return ans;
    }
}
