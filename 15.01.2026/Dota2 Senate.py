class Solution(object):
    def predictPartyVictory(self, senate):
        senate = list(senate)
        length = len(senate)
        radiant_queue, dire_queue = deque(), deque()
        for  i in range(length):
            if senate[i] == "R":
                radiant_queue.append(i)
            elif senate[i] == "D":
                dire_queue.append(i)
        while radiant_queue and dire_queue:
            R_var_index = radiant_queue.popleft()
            D_var_index = dire_queue.popleft()
            if R_var_index < D_var_index :
                radiant_queue.append( R_var_index + length)
            else:
                dire_queue.append( D_var_index + length)
        if len(radiant_queue) > len(dire_queue):
            return "Radiant"
        else:
            return "Dire"
