class Solution(object):
    def dailyTemperatures(self, n):
        l1=[]
        l2=[]
        k=[0]*len(n)
        p=0
        for i in range(len(n)):
            if i==0 or len(l2)<1:
                l1.append(i)
                l2.append(n[i])
            else:
                if n[i]<=l2[-1]:
                    l1.append(i)
                    l2.append(n[i])
                else:
                    while True:
                        if len(l2)<1 or len(l1)<1:
                            l1.append(i)
                            l2.append(n[i])
                            break
                        if n[i]>l2[-1]:
                            k[l1[-1]]=i-l1[-1]
                            l1.pop()
                            l2.pop()
                        else:
                            l1.append(i)
                            l2.append(n[i])
                            break
        return k
        
