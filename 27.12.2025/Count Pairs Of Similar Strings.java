class Solution {
    public int similarPairs(String[] words) {
        List<boolean[]> alphabetArrayList = new ArrayList<>();
        int similarWordPaircount=0;

        for(String word:words) {
            boolean[] alphabetArray = findAlphabetsInWord(word);
                        
            for(boolean[] uniqueAlphabetArray:alphabetArrayList) {
                if(Arrays.equals(alphabetArray, uniqueAlphabetArray)) {
                    similarWordPaircount++;
                }
            }
            alphabetArrayList.add(alphabetArray);
        }
        return similarWordPaircount;
    }

    static boolean[] findAlphabetsInWord(String word) {
     boolean[] alphabetArray = new boolean[26];
     for(int i=0;i<word.length();i++) {
          alphabetArray[word.charAt(i)-'a'] = true;
     }
     return alphabetArray;
    }
}
