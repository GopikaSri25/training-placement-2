class Solution {
    public int[] decimalRepresentation(int n) {
        int dec=1;
        int num=0;
        List<Integer> ls=new ArrayList<>();
        while(n>0){
            num = (n%10)*dec;
            if(num!=0){
                ls.add(num);            }
            
            dec=dec*10;
            n/=10;
        }

        Collections.sort(ls, Collections.reverseOrder());
        int[] ans=new int[ls.size()];
        int i=0;
        for(int num1:ls){
            ans[i++]=num1;
        }
        return ans;

    }
}
