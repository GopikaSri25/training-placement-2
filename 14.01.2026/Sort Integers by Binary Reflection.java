class Solution {
    public int[] sortByReflection(int[] nums) {
        int n=nums.length;
        Integer[] arr=new Integer[n];
        for(int i=0;i<n;i++) arr[i]=nums[i];
        Arrays.sort(arr, (a,b) ->{
            int ra=reflect(a);
            int rb=reflect(b);
            if(ra != rb) return ra-rb;
            return a-b;
        });
        for(int i=0;i<n;i++){
            nums[i]=arr[i];
        }
        return nums;
    }
    private int reflect(int x) {
        int r = 0;
        while (x > 0) {
            r = (r << 1) | (x & 1);
            x >>= 1;
        }
        return r;
    }
}
