class Solution(object):
    def minSteps(self, n):
        if n == 1:
            return 0

        l = [float('inf')] * (n+1)
        l[1] = 0  

        for j in range(1, n+1):
            steps = l[j]
            k = j
            count = 1
            while k + j <= n:
                if count == 1:
                    steps += 2
                else:
                    steps += 1
                k += j
                l[k] = min(l[k], steps)
                count += 1

        return l[n]
