class Solution(object):
    def numberOfPoints(self, A):
        A.sort()
        s = A[0][0]
        e = A[0][1]
        ans = []
        for i in range(1,len(A)):
            s_new = A[i][0]
            e_new = A[i][1]      

            if s_new > e :
                ans.append([s,e])
                s = s_new
                e = e_new
            else:
                if s_new < s:
                    s = s_new
                if e_new > e:
                    e = e_new
        
        ans.append([s,e])

        total = 0
        for i in range(0,len(ans)):
            s = ans[i][0]
            e = ans[i][1]
            l = e - s + 1
            total += l

        return total
        
