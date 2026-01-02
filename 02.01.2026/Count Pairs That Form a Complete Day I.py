class Solution(object):
    def countCompleteDayPairs(self, hours):
        count = 0
        index_i = 0
        for i in hours[:-1]:
            index_j = index_i + 1
            for j in hours[index_j:]:
                if (i + j) % 24 == 0:
                    count += 1
                index_j += 1
            index_i += 1
        return count
