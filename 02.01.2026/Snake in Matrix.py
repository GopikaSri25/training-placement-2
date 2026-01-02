class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        i,j = 0,0
        for com in commands:
          if com == "RIGHT":
            j +=1
          elif com == "LEFT":
            j -=1
          elif com == "DOWN":
            i +=1
          elif com =="UP":
            i -=1
        return i*n+j
        
