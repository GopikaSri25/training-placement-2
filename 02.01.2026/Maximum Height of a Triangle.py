class Solution:
    def findMaxHeight(self, red, blue):
        balls_on_line = 1
        is_red = True

        while red > 0 or blue > 0:
            if is_red and red >= balls_on_line:
                red -= balls_on_line
            elif not is_red and blue >= balls_on_line:
                blue -= balls_on_line
            else:
                break
            is_red = not is_red
            balls_on_line += 1

        return balls_on_line - 1

    def maxHeightOfTriangle(self, red, blue):
        return max(self.findMaxHeight(red, blue), self.findMaxHeight(blue, red))
