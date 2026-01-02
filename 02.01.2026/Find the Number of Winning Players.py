class Solution(object):
    def winningPlayerCount(self, n, pick):
        ret = []
        for i in range(n):
            ret.append([])
        for p in pick:
            ret[p[0]].append(p[1])
        count = 0
        index = 0
        for x in ret:
            found = 0
            sx = list(set(x))
            lsx = len(sx)
            index_in = 0
            while found == 0 and index_in < lsx:
                if x.count(sx[index_in]) > index:
                    count += 1
                    found = 1
                index_in += 1
            index += 1
        #print ret
        return count
