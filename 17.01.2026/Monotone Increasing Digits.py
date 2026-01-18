class Solution(object):
    def monotoneIncreasingDigits(self, n):
        d = []

        while n > 0:
            d.append(n%10)
            n /= 10
        
        d = d[::-1]
        
        p1, p2 = 0, 0
        st = -1
        dt = {}

        while p1 < len(d) - 1:

            if d[p1] > d[p1 + 1]:
                if d[p1] in dt:
                    st = dt[d[p1]]
                    print('in', st)
                else:
                    st = p1
                break
            if d[p1] == d[p1+1]:
                if d[p1] not in dt:
                    dt[d[p1]] = p1
            p1 += 1
        if st != -1:
            d[st] -= 1
            st += 1
            while st < len(d):
                d[st] = 9
                st += 1
        
        rt = 0
        for i in d:
            rt = rt * 10 + i
        return rt
