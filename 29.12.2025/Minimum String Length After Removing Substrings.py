class Solution(object):
    def minLength(self, s):
        min_len = []
        i=0
        for char in s:
            if min_len and (min_len[-1] + char == 'AB' or min_len[-1] + char == 'CD'):
                min_len.pop()
            else:
                min_len.append(char)
                
        return len(min_len)

obj = Solution()
print(obj.minLength("ABFCACDB"))
