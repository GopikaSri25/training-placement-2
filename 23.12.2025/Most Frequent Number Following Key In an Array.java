class Solution {
    public int mostFrequent(int[] nums, int key) {
        int n = nums.length, max_val = 0, m_val = 0;

        HashMap<Integer,Integer> dict1 = new HashMap<>();

        for (int i = 0; i < n-1; i++){
            if (nums[i] == key){
                if (!dict1.containsKey(nums[i+1])){
                    dict1.put(nums[i+1],1);
                    max_val = Math.max(max_val,1);
                } else {
                    dict1.put(nums[i+1],dict1.get(nums[i+1])+1);
                    max_val = Math.max(max_val,dict1.get(nums[i+1]));
                }
            }
        }

        for (int v: dict1.keySet()){
            if (dict1.get(v) == max_val){
                m_val = v;
            }
        }

        return m_val;
    }
}
