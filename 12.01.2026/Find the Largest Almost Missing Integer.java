class Solution {
    public int largestInteger(int[] nums, int k) {
        int ans = Integer.MIN_VALUE; 
        if(k == nums.length){
            for(int i = 0 ; i  < nums.length ; i++){
                ans = Math.max(ans , nums[i]);
            }
            return ans; 
        }
        if(k == 1){
            HashMap<Integer , Integer> map = new HashMap<>(); 
            for(int num : nums){
                if(!map.containsKey(num)){
                    map.put(num , 1);
                }
                else{
                    map.put(num , 1 + map.get(num));
                }
            }
            for(Integer key : map.keySet()){
                if(map.get(key) == 1){
                    ans = Math.max(ans , key);
                }
            }
            return ans == Integer.MIN_VALUE ? -1 : ans; 
        }
        int si = 0; 
        int ei = -1; 
        for(int i = nums.length - 1 ; i >  0 ; i--){
            if(nums[i] == nums[si]){
                ei = i; break; 
            }
        }
        if(ei == -1){
            ans = Math.max(ans , nums[0]);
        }
        ei = nums.length - 1; 
        si = -1; 
        for(int i = 0 ; i < nums.length - 1 ; i++){
            if(nums[i] == nums[ei]){
                si = i; break; 
            }
        }
        if(si == -1){
            ans = Math.max(ans , nums[nums.length - 1]);
        }
        return ans == Integer.MIN_VALUE ? -1 : ans; 

    }
}
