class Solution(object):
    def tree2str(self, root):
        res = []
        self.dfs(root, res)
        return ''.join(res)

    def dfs(self, root, res):
        if root is None:
            return

        res.append(str(root.val))

        if root.left is None and root.right is None:
            return

        res.append('(')
        self.dfs(root.left, res)
        res.append(')')

        if root.right is not None:
            res.append('(')
            self.dfs(root.right, res)
            res.append(')')
