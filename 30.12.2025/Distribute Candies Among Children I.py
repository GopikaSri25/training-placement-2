class Solution(object):
    def distributeCandies(self, n, limit):
        ways=0
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    if i+j+k==n:
                        ways+=1
        return ways
