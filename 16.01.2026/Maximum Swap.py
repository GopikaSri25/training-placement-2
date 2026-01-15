class Solution(object):
    def maximumSwap(self, num):
        orig=num
        arr=[]
        while num>0:
            digit=num%10
            num//=10
            arr.append(digit)
        arr.reverse()
        des=[orig]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                s=""
                arr[i],arr[j]=arr[j],arr[i]
                for d in arr:
                    s+=str(d)
                des.append(int(s))
                arr[i],arr[j]=arr[j],arr[i]
        des.sort(reverse=True)
        return des[0]
        
                
        


        
        
