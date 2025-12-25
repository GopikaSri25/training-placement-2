class Solution {

    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int requiredEnergy = 0;
        int energyDiff = 0;

        for (int num : energy) {
            requiredEnergy += num;
        }

        if (requiredEnergy >= initialEnergy) {
            energyDiff = requiredEnergy - initialEnergy + 1;
        }

        int additionalExperience = 0;

        for (int num : experience) {

            if (initialExperience <= num) {
                int addition = num - initialExperience + 1;
                additionalExperience += addition;
                initialExperience += addition;
            }

            initialExperience += num;
        }

        return energyDiff + additionalExperience;
    }
}
