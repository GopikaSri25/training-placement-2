class Solution {
    public int findMiddleIndex(int[] arr) {
      int n=arr.length;
        int[] prefix_sum=new int[n];
        prefix_sum[0]=arr[0];
        for(int i=1;i<n;i++)
        {
            prefix_sum[i]=arr[i]+prefix_sum[i-1];
        }
        for(int i=0;i<n;i++)
        {
          int before=0,after=0;
          if(i>0)
           before=prefix_sum[i-1];
           if(i<n)
           after=prefix_sum[n-1]-prefix_sum[i];
          if(before==after) return i;
         
        }
        return -1;   
    }
}
