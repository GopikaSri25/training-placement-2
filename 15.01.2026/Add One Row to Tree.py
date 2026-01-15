from collections import deque
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """
        if(depth == 1):
            return TreeNode(val, root)
        q = deque()
        q.append(root)
        q.append(None)
        cnt = 2
        while(len(q)>0):
            if(q[0]==None and len(q)>1):
                q.append(None)
                q.popleft()
                cnt+=1
            if(cnt==depth):
                while(len(q)>0):
                    if(q[0]!=None):
                        q[0].left = TreeNode(val, q[0].left, None)
                        q[0].right = TreeNode(val, None, q[0].right)
                    q.popleft()
                break
            elif(q[0]!=None):
                if(q[0].left!=None): q.append(q[0].left)
                if(q[0].right!=None): q.append(q[0].right)
            q.popleft()
        return root
