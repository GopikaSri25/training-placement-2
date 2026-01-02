class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):

        p ='aceg'
        s = 'bdfh'
        k=[]
        cor = [coordinate1,coordinate2]
        for i in cor:
            if i[0] in p and int(i[1])%2==0:
                k.append('White')
            elif i[0] in p and int(i[1])%2!=0:
                k.append('Black')
            elif i[0] in s and int(i[1])%2!=0:
                k.append('White')
            else:
                k.append('Black')
        if k[0] == k[1]:
            return True
        else:
            return False

        
