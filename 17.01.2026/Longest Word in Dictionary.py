class Solution(object):
    def longestWord(self, words):
        while len(words)>0:
            longest=""
            for w in words:
                if len(w)>len(longest):
                    longest=w
                if len(w)==len(longest) and w<longest:
                    longest=w
            can_build=True
            for i in range(1,len(longest)):
                temp=longest[:i]
                if temp not in words:
                    can_build=False
                    break
            if can_build==True:
                return longest
            words.remove(longest)
        return ""

