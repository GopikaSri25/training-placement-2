class Solution {
    public boolean checkPrimeFrequency(int[] nums) {
        int[] freq =  new int[101];

        HashSet<Integer> prime = new HashSet<>();
        int[] primes= {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97};

        for(int i : primes){
            prime.add(i);
        }

        for(int i : nums){
            freq[i]++;
        } 

        for(int i : freq){
            if(i>1 && prime.contains(i)){
                return true;
            }
        }

        return false;
    }
}
