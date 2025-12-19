class Solution {
    public int[] getConcatenation(int[] b) {
      int size=2*b.length;
int[] a=new int[size];
System.out.println(a.length);
        System.arraycopy(b,0,a,0,b.length);
        System.arraycopy(b,0,a,b.length ,b.length);  
        return a;
    }
}
