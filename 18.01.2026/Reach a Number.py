class Solution(object):
    def reachNumber(self, target):
        target=abs(target)
        step=0
        sum_steps=0
        while sum_steps < target or (sum_steps-target)%2!=0:
            step+=1
            sum_steps+=step
        return step
        
