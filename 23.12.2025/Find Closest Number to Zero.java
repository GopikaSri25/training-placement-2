class Solution {
  public int findClosestNumber(int[] nums) {
    Integer minIndex = null;
    int minAbs = Integer.MAX_VALUE;
    boolean wasNegative = true;

    for (int i = 0; i < nums.length; i++) {
      int abs = Math.abs(nums[i]);
      if (abs < minAbs) {
        minIndex = i;
        minAbs = abs;
        wasNegative = nums[i] < 0;
      }
      else if (abs == minAbs && wasNegative && nums[i] > 0) {
        minIndex = i;
        wasNegative = false;
      }
    }

    return nums[minIndex];
  }
}
