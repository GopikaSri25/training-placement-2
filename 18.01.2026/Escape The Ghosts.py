class Solution(object):
    def escapeGhosts(self, ghosts, target):
        return min([abs(g[0]-target[0]) + abs(g[1]-target[1]) for g in ghosts]) > abs(target[0]) + abs(target[1])
        
        
