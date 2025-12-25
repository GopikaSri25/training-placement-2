class Solution {
    public int minimumOperations(int[] nums) {
        if(nums.length == 1 && nums[0] == 0)
         {return 0;}
        if (nums.length == 1) {return 1;}
        Set<Integer> seen = new HashSet<>();   
        
        for (int x  : nums) {
            if (x > 0 && !seen.contains(x)) { 
                seen.add(x);        
            }
        }
        return seen.size(); 
    }
}
