class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        i = left 
        while i <= right :
            check = words[i]
            if check[0] in vowels and check[-1] in vowels:
                count += 1
            i += 1
        
        return count
        
