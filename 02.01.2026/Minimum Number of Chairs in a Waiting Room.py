class Solution(object):
    def minimumChairs(self, s):
        m = 0
        chair = 0
        for i in s:
            if i == 'E':
                chair+= 1
                m = max(m,chair)
            else:
                chair -= 1
                m = max(m,chair)
        return m

        
