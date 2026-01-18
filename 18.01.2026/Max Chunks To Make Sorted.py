class Solution(object):
    def maxChunksToSorted(self, arr):
        n = len(arr)
        h = set()
        pos = 0
        ans = n
        for i in range(n):
            if arr[i] == pos:
                h.add(pos)
                pos += 1
                while pos in h:
                    pos+=1
                if pos <= i and pos not in h:
                    ans -= 1
            else:
                ans-=1
                h.add(arr[i])
        return ans
            
