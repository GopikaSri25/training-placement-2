class Solution {
    public int sumDivisibleByK(int[] nums, int k) {
        int count=0;
        HashMap<Integer,Integer>hm=new HashMap<>();
        for(int n: nums)
        {
            hm.put(n, hm.getOrDefault(n,0)+1);
        }
        for(Map.Entry<Integer,Integer>map : hm.entrySet())
        {
           int key= map.getKey();
           int val= map.getValue();
           if(val % k == 0)
           {
            count+=key*val;
           }
        }
        return count;
    }
}
