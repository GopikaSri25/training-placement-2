class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        max_width = 0
        queue = deque([(root, 0)])
        while queue:
            level_size = len(queue)
            leftmost_index = queue[0][1]
            rightmost_index = leftmost_index
            for _ in range(level_size):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, (2 * i) + 1))
                if node.right:
                    queue.append((node.right, (2 * i) + 2))
                rightmost_index = i
            level_width = (rightmost_index - leftmost_index) + 1
            if level_width > max_width:
                max_width = level_width
        return max_width
