class Solution(object):
    def printTree(self, root):
        def high(r):
            if not r:
                return 0
            left, right = high(r.left), high(r.right)
            return 1 + max(left, right)
        length = high(root)
        width = 1 
        power = 2
        for i in range(length-1):
            width += power
            power *= 2
        ans = [[""]*width for i in range(length)]
        def check(r, left, right, lvl):
            if not r:
                return
            place = (left+right)//2
            ans[lvl][place] =str(r.val)
            check(r.left, left, place, lvl+1)
            check(r.right, place, right, lvl+1)
        check(root, 0, width, 0)
        return ans


            
            
        
