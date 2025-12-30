class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        c=0
        for i in hours:
            if i>= target:
                c=c+1
        return c

        
