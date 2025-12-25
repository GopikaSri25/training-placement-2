class Solution {
    public boolean findSubarrays(int[] nums) {
          Set<Integer> set = new HashSet<>();
        for(int i =0;i<nums.length;i++){
            int sum =0;
            try {
                sum += nums[i] + nums[i + 1];
                if (!set.add(sum)) {
                    return true;
                }

            }
            catch (Exception e){
                continue;
            }

        }
        return false;
    }
}
