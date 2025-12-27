class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        bulky=heavy=False
        if((length>=10000 or width>=10000 or height>=10000 or mass>=10000) or (length*width*height>=1000000000)):
            bulky=True
        if(mass>=100):
            heavy=True
        if(bulky and heavy):
            return "Both"
        if(bulky and not heavy):
            return "Bulky"
        if(heavy and not bulky):
            return "Heavy"
        return "Neither"
