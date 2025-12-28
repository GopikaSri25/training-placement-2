class Solution(object):
    def total(self,player):
        total_score = 0
        for i in range(len(player)):
            if(i > 0 and player[i-1 ]==10) or (i > 1 and player[i-2 ]==10):
                total_score+= 2*player[i]
            else:
                total_score+=player[i]

        return total_score
            

    def isWinner(self, player1, player2):
        ans=0
        player1val=self.total(player1)
        player2val=self.total(player2)
        if player1val> player2val:
            ans=1
        elif player1val < player2val:
            ans=2
        return ans


        
            
            


        
