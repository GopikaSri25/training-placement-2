class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        distance=0
        while mainTank>=5:
            mainTank-=5
            distance+=50
            if additionalTank>0:
                additionalTank-=1
                mainTank+=1
        return 10*mainTank+distance
