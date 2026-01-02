class Solution(object):
    def minChanges(self, n, k):
        nb = bin(n)[2:]
        kb = bin(k)[2:]
        ln = len(nb)
        lk = len(kb)
        if ln < lk:
            return -1
        else:
            while len(kb) < ln:
                kb = "0" + kb
            index = 0
            counter = 0
            for i in nb:
                if i == "0" and kb[index] == "1":
                    return -1
                if i == "1" and kb[index] == "0":
                    counter += 1
                index += 1
            return counter
