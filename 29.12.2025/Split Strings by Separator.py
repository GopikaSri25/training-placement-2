class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        a = []
        for i in words:
            a.extend(i.split(separator))
        b = []
        for i in a:
            if i!="":
                b.append(i)
        return b
