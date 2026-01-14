class Solution {
    public int findNthDigit(int n) {
        int digit = 1;
        long start = 1;
        long count = 9;

        while (n > digit * count) {
            n -= digit * count;
            digit += 1;
            count *= 10;
            start *= 10;
        }

        long num = start + (n - 1) / digit;
        return String.valueOf(num).charAt((n - 1) % digit) - '0';
    }
}
