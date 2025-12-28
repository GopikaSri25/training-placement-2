class Solution(object):
    def evenOddBit(self, n):
        eve = 0
        odd = 0 
        x = bin(n)[2:][::-1]
        for i in range(0,len(x)):
            if i%2==0 and x[i]=="1":
                eve += 1
            elif i%2!=0 and x[i]=="1":
                odd += 1
        return [eve,odd]
