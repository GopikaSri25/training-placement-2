class Solution(object):
    def finalString(self, s):
        res=""
        for ch in s:
            if ch!="i":
                res+=ch

            else:
                res=res[::-1]
        return res
