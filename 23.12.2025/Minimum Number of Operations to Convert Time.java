class Solution {
    public int convertTime(String current, String correct) {
        int currHours = Integer.parseInt(current.substring(0, 2));
        int corrHours = Integer.parseInt(correct.substring(0, 2));
        int diffHours = corrHours - currHours;

        int currMins = Integer.parseInt(current.substring(3, 5));
        int corrMins = Integer.parseInt(correct.substring(3, 5)); 

        int diffMins = corrMins - currMins;

        if (diffMins == 0) return diffHours;
        else if (diffMins > 0) {
            return calculateMinuteSteps(diffMins) + diffHours;
        } else {
            diffHours--;  // negativ minutes
            int restMins = 60 - currMins + corrMins;
            return calculateMinuteSteps(restMins) + diffHours;
        }
    }

    private int calculateMinuteSteps(int minutes) {
        int min15 = minutes / 15;
        int rest1 = minutes % 15;

        int min5 = rest1 / 5;
        int rest2 = rest1 % 5;

        int min1 = rest2;

        return min15 + min5 + min1;
    }
}
