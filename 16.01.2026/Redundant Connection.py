class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        root = [i for i in range(n)]
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(a,b):
            rootA , rootB = find(a), find(b)
            if rootA != rootB:
                root[rootB] = rootA
                return False
            else:
                return True
        
        for [a,b] in edges:
            if union(a-1,b-1):
                return [a,b]
        
        return [0,0]

        
