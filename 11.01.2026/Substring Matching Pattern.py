class Solution(object):
    def hasMatch(self, s, p):
        pattern1, pattern2 = p.split('*')

        i = 0
        while i < len(s):
            if s[i: i + len(pattern1)] != pattern1:
                i += 1
            else:
                if len(pattern2) == 0:
                    return True
                else:
                    j = i + len(pattern1)
                    while j < len(s):
                        if s[j: j + len(pattern2)] != pattern2:
                            j += 1
                        else:
                            return True
                    return False
        return False
