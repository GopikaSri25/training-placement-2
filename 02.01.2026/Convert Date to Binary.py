class Solution(object):
    def convertDateToBinary(self, date):
        d=date.split("-")
        s=""
        for i in d:
            s+=str(bin(int(i)))[2:]+"-"
        return (s[:len(s)-1])
        
        
