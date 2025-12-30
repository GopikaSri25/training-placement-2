class Solution(object):
    def canBeEqual(self, s1, s2):
        count = 0
        for i in range(2):
            if (ord(s1[i]) + ord (s1[i+2])== ord(s2[i]) + ord(s2[i+2])) \
            and (s1[i] == s2[i] or s1[i]==s2[i+2]):
                count +=1
        return count == 2
