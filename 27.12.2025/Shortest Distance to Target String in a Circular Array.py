class Solution(object):
    def closestTarget(self, words, target, startIndex):
        if words[startIndex] == target: 
            return 0 
        
        n = len(words)

        ptr1 = (startIndex - 1) % n
        ptr1_count = 1

        ptr2 = (startIndex + 1) % n
        ptr2_count = 1 

        while ptr1 != startIndex and ptr2 != startIndex:

            if words[ptr1] == target: 
                return ptr1_count

            if words[ptr2] == target:
                return ptr2_count 

            ptr1 = (ptr1 - 1) % n
            ptr2 = (ptr2 + 1) % n

            ptr1_count += 1 
            ptr2_count += 1 

        return -1 
