class Solution {
    public int[] numberOfPairs(int[] nums) {
   int fre[]=new int[101];
     int res[]=new int[2];
     for(int n:nums){
       fre[n]++;
        }
        int count=0;
        int l=0;
     for(int p:fre){
          int m=p;
          while(m>1){
           count++;
           m=m-2;
          }
          if(m==1){
               l++;
          }

        }
        res[0]=count;
        res[1]=l;
        return res;
    }
}
