class Solution(object):
    def getLongestSubsequence(self, words, groups):
        n = len(words)
        seq0 = []  
        seq1 = []  

        for i in range(n): 
            word = words[i]
            group = groups[i]

            if group == 0:
                if len(seq1) + 1 > len(seq0):
                    seq0 = seq1 + [word]
                else:
                    seq0 = seq0 if len(seq0) >= 1 else [word]
            else: 
                if len(seq0) + 1 > len(seq1):
                    seq1 = seq0 + [word]
                else:
                    seq1 = seq1 if len(seq1) >= 1 else [word]

        # Return the longer of the two sequences
        return seq0 if len(seq0) >= len(seq1) else seq1
        
