class Solution(object):
    def minimumBoxes(self, apple, capacity):
        n=sum(apple[0:])
        capacity.sort(reverse=True)
        c=capacity[0]
        count=1
        for i in range(1,len(capacity)+1):
            if c>=n:
                return count
            else:
                c=c+capacity[i]
                count+=1
        
 
