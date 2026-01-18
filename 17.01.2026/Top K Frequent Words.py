class Solution(object):
    def topKFrequent(self, words, k):
        wordFreq = {}
        for elem in words:
          wordFreq[elem] = wordFreq.get(elem,0) + 1
        ls = sorted(list(wordFreq.items()),key = lambda val:(-val[1],val[0]))
        res = [ls[i][0] for i in range(k)]
        return res
        

        
