class Solution(object):
    def buttonWithLongestTime(self, events):
        events.insert(0, [0, 0])

        maxInd = events[0][0]
        macks = events[0][1]

        for i in range(1, len(events)):
            calc = events[i][1] - events[i-1][1]
            if (calc > macks):
                macks = calc
                maxInd = events[i][0]
            elif (calc == macks):
                maxInd = min(events[i][0], maxInd)

        return maxInd
            
