import heapq

class Solution(object):
    def reorganizeString(self, s):
        count = {}

        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        pq = []

        for key, val in count.items():
            heapq.heappush(pq, (val*(-1), key))
        
        string = ""

        while pq:
            freq, char = heapq.heappop(pq)

            if string == "" or char != string[-1]:
                string += char

                if freq*(-1) > 1:
                    heapq.heappush(pq, (freq + 1, char))
            else:
                if not pq:
                    return "" 
                    
                freq2, char2 = heapq.heappop(pq)
                string += char2

                if freq2*(-1) > 1:
                    heapq.heappush(pq, (freq2 + 1, char2))
                
                heapq.heappush(pq, (freq, char))
        return string

        
