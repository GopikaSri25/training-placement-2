class Solution {
    public int distinctAverages(int[] nums) {
        Arrays.sort(nums);
        ArrayList<Float> r=new ArrayList<>();
        int i,n=nums.length,t;
        for(i=0;i<n/2;i++){
            t=nums[i]+nums[n-i-1];
            r.add(t/2.0f);
        }
        Collections.sort(r);
        ArrayList<Float> u=new ArrayList<>();
        for(float x:r){
            if(!u.contains(x)) u.add(x);
        }
        return u.size();
    }
}
