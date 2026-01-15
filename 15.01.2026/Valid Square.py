import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def euclidean_distance(p1,p2):
            x1, y1 = p1
            x2, y2 = p2
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            return dist
        
        dist = []
        points = [p1, p2, p3, p4]
        for i in range(0,3):
            for j in range(i+1,4):

                point_1 = points[i]
                point_2 = points[j]
                current = euclidean_distance(point_1, point_2)
                dist.append(current)

        if len(set(dist)) == 2 and 0 not in set(dist):
            return True
        else:
            return False
