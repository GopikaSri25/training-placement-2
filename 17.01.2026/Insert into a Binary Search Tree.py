class Solution(object):
    def insertIntoBST(self, root, val):
        self.inorder = []

        if not root:
            return TreeNode(val)

        def helper(root, node):
            if not node:
                return 

            if val < node.val:
                helper(root, node.left)
            else:
                helper(root, node.right)

            if not node.left and val < node.val:
                node.left = TreeNode(val)
            elif not node.right and val > node.val:
                node.right = TreeNode(val)

            return root

        ret = helper(root, root)
        return ret
