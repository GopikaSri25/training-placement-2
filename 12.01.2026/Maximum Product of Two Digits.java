class Solution {
    public int maxProduct(int n) {
        int count=0;
        int original=n;
        while(original!=0){
            original/=10;
            count++;
        }
        int[] arr=new int[count];
        int index=0;
        while(n!=0){
            int digit=n%10;
            arr[index++]=digit;
            n/=10;
        }
        Arrays.sort(arr);
        return arr[arr.length-1]*arr[arr.length-2];
    }
}
