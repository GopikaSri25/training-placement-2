class Solution(object):
    def generateKey(self, num1, num2, num3):
        s1 = str(num1)
        s2 = str(num2)
        s3 = str(num3)
        s1 = "0" * (4 - len(s1)) + s1
        s2 = "0" * (4 - len(s2)) + s2
        s3 = "0" * (4 - len(s3)) + s3
        print s1
        print s2
        print s3
        dig1 = min([s1[0],s2[0],s3[0]])
        dig2 = min([s1[1],s2[1],s3[1]])
        dig3 = min([s1[2],s2[2],s3[2]])
        dig4 = min([s1[3],s2[3],s3[3]])
        return int(str(dig1) + str(dig2) + str(dig3) + str(dig4))
