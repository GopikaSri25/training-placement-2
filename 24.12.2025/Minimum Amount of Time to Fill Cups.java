class Solution {
    public int fillCups(int[] amount) {

        int max = 0;
        int sum = 0;
        for (int num : amount) {

            sum += num;
            max = Math.max(num, max);
        }
        if (sum == amount[0] || sum == amount[1] || sum == amount[2])
            return sum;

        int cnt = 0;

        while (sum > 0) {

            sum = sum - 2;
            max = Math.max(0,max - 1);

            cnt++;
            if (sum == max)
                return cnt + max;
        }
        return cnt;

    }
}
