class Solution {
    public int smallestAbsent(int[] nums) {
        boolean[] seen = new boolean[101];
        int sum = 0;
        for(int i : nums) {
            if(i > 0) {
                seen[i] = true;
            }
            sum += i;
        }

        int avg = sum / nums.length;
        if(avg < 0) {
            avg = 0;
        }

        for(int i = avg + 1; i <= 100;i++) {
            if(!seen[i]) {
                return i;
            }
        }

        return 101;
    }
}
