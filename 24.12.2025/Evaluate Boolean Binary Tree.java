class Solution {
    boolean tree(TreeNode root)
    {
        if(root.val == 0) return false;
        if(root.val == 1) return true;

        if(root.val == 2){
            boolean a = tree(root.left);
            boolean b = tree(root.right);

            return a||b;
        } 
        boolean a = tree(root.left);
        boolean b = tree(root.right);
        return a&&b;
    }
    public boolean evaluateTree(TreeNode root) {
        return tree(root);
    }
}
