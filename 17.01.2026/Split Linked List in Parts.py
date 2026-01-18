class Solution(object):
    def splitListToParts(self, head, k):
        s = 0
        curr = head
        while curr:
            s += 1
            curr = curr.next
        sp = s // k
        r = s % k
        ds = [None] * k
        curr = head 
        for i in range(k):
            ds[i] = curr
            size = sp + (1 if r > 0 else 0)
            if r > 0:
                r -= 1
            for _ in range(size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        
        return ds
