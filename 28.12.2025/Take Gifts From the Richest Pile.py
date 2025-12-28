import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        max_heap = [ -gift for gift in gifts ]
        heapq.heapify(max_heap)
        for _ in range(k):
            max_gift = -(heapq.heappop(max_heap))
            reduced_gift = int(math.sqrt(max_gift))
            heapq.heappush(max_heap, -reduced_gift)

        total = -(sum(max_heap))  
        return total  
            


        
