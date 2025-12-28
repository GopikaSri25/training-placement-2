class Solution(object):
    def rowAndMaximumOnes(self, mat):
        row_index=0
        max_cnt=0
        for i in range(len(mat)):
            cnt=Counter(mat[i])[1]
            if cnt>max_cnt:
                max_cnt=cnt
                row_index=i
        return [row_index,max_cnt]
