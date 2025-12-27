class Solution
 {
    public int pivotInteger(int n) 
    {
        int i=1,k,sum=1;
        int[] forward = new int[n];
        int[] backward =new int[n];
        forward[0]=1;
        backward[n-1]=1;
        while(i<=n-1)
        {
         sum+=i+1;
         forward[i]=sum;
         i++;
        }
        i=n-2;
        sum=n;
         while(i>0)
        {
         sum+=i+1;
         backward[i]=sum;
         i--;
        }
        for(k=0;k<n;k++){
            if(forward[k]==backward[k])
            return k+1;
        }
        
        return -1;
    }
}
