class Solution(object):
    def circularGameLosers(self, n, k):
        Start = 1
        i = 1
        recieved = [Start]
        
        while True:
            Next = (Start + i * k) % n
            if Next == 0:
                Next = n
                
            if Next in recieved:
                break
            else:
                recieved.append(Next)
                i += 1
                Start = Next
        
        losers = []
        for j in range(n):
            if j + 1 not in recieved:
                losers.append(j + 1)
        
        return losers
