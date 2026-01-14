class Solution {
    public String reversePrefix(String s, int k) {
        if(k > s.length()){
           return s;
        }
        int left = 0, right = k-1;
        char [] charArr = s.toCharArray();
        while(left < right){
          char temp = charArr[left];
          charArr[left] = charArr[right];
          charArr[right] = temp;
          left++;
          right--;
        }
        return new String(charArr);
    }
}
