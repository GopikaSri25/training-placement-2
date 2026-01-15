class Solution(object):
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        
        def serialize(node):
            if not node:
                return "#"
            
            subtree = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
            
            subtree_map[subtree] += 1
            if subtree_map[subtree] == 2:
                result.append(node)
            
            return subtree
        
        subtree_map = defaultdict(int)
        result = []
        
        serialize(root)
        
        return result
