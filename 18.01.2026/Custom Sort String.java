class Solution {
    public String customSortString(String order, String s) {
        String f = "";

        for (char y : order.toCharArray()) {
            for (char z : s.toCharArray()) {
                if (y == z) {
                    f += y;
                }
            }
        }

        for (char z : s.toCharArray()) {
            if (!order.contains(String.valueOf(z))) {
                f += z;
            }
        }

        return f;
    }
}
