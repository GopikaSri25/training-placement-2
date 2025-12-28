class Solution(object):
    def passThePillow(self, n, time):
        person=direction=1
        while time>0:
            person+=direction
            time-=1
            if person==n or person==1:
                direction*=-1
        return person
