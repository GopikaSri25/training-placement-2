class Solution {
    public boolean scoreBalance(String s) {
       int leftSum = s.charAt(0) - 'a' + 1, rightSum = s.charAt(s.length() - 1) - 'a' + 1;
        int i = 1, j = s.length() - 2;
        while (i <= j) {
            if (leftSum <= rightSum) {
                leftSum += s.charAt(i) - 'a' + 1;
                i++;
            } else if (leftSum > rightSum) {
                rightSum += s.charAt(j) - 'a' + 1;
                j--;
            }
        }
        return leftSum == rightSum;
    }
}
