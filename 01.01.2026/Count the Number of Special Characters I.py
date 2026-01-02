class Solution(object):
    def numberOfSpecialChars(self, word):
        set_val0=set()
        set_val1=set()
        count=0
        for i in word:
            if(i.islower()):
                set_val0.add(i)
            else:
                set_val1.add(i)
        low_val=list(set_val0)
        up_val=list(set_val1)
        for i in range(len(low_val)):
            for j in range(len(up_val)):
                if(ord(low_val[i])-32 == ord(up_val[j])):
                    count+=1
        
        return count
