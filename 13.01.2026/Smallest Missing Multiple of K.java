class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> hs=new HashSet<>();

        for(int num:nums){
            hs.add(num);
        }

        int i=1;
        int num=k*i;
        while(hs.contains(num)){
            i++;
            num=k*i;
        }

        return num;
    }
}
