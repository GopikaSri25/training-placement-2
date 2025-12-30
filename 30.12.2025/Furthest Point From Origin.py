class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
            
        
