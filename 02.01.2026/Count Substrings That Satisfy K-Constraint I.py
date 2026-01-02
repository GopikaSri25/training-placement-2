class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        i = 0
        count_zero = 0
        count_one = 0
        count = 0

        for j in range(len(s)):
            if s[j] == "0":
                count_zero += 1
            else:
                count_one += 1

            while count_zero > k and count_one > k:
                if s[i] == "0":
                    count_zero -= 1
                else:
                    count_one -= 1

                i+=1

            count += (j - i +1)


        return count
