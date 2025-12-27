class Solution(object):
    def captureForts(self, forts):
        l = 0
        r = 1
        c = 0
        o = 0
        if len(forts) == 0:
            return 0

        while r < len(forts):
            while l < len(forts) and (forts[l] != -1 and forts[l] != 1):
                l += 1

            if l < len(forts):
                if forts[l] == -1:
                    o = 1
                else:
                    o = -1
            else:
                return c

            while r < len(forts) and forts[r] != o:
                if forts[r] == forts[l]:
                    l = r
                r += 1
            
            if r < len(forts) and forts[r] == o:
                c = max((r-l-1),c) 
            l = r
            r += 1
            
            
        return c
            

        
