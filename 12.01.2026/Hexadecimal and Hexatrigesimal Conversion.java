class Solution {
    public String concatHex36(int n) {
        long n2 = n * n;
        long n3 = n2 * n;

        String hexaDi = Long.toHexString(n2); 
        String hexaTri = Long.toString(n3, 36);

        return (hexaDi + hexaTri).toUpperCase();
    }
}
