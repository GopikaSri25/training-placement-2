class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        t=[len(s1),len(s2),len(s3)]
        i=0
        f=False
        while True:
            try:
                if s1[i]==s2[i]==s3[i]:
                    f=True
                    i+=1
                    continue
                else:
                    if not f:
                        return -1
                    
                    return sum(t)-3*i
            except:
                break
        t.sort()
        return t[2]+t[1]-2*t[0]
      
        
