class Solution {
    public int minimumDistance(int[] nums) {
        int n=nums.length;
        int sum=1000;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j)continue;
                for(int k=0;k<n;k++){
                    if(j==k||i==k)continue;
                    else{
                        if(nums[i]==nums[j]&&nums[j]==nums[k]){
                            int a=i-j;
                            int b=j-k;
                            int c=k-i;                           
                            if(a<0)a=-a;
                            if(b<0)b=-b;
                            if(c<0)c=-c;
                            if(sum>a+b+c)sum=a+b+c;
                        }
                    }
                }
            }
        }
        if(sum==1000)return -1;
        return sum;
    }
}
