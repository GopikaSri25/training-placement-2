class Solution(object):
    def __init__(self):
        self.longest = 0

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left) if (root.left and root.val == root.left.val) else 0
        right = self.depth(root.right) if (root.right and root.val == root.right.val) else 0
        pathLength = left + right
        if pathLength > self.longest:
            self.longest = pathLength
        return 1 + max(left, right)

    def traverse(self, root):
        if not root:
            return
        self.depth(root)
        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)


    def longestUnivaluePath(self, root):
        self.traverse(root)
        return self.longest
