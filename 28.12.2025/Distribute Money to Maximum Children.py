class Solution(object):
    def distMoney(self, money, children):
        if money < children:
            return -1
        else:
            if money < 8:
                if money == 1:
                    return -1
                if money == 4 and children == 1:
                    return -1
                else:
                    return 0
            else:
                chunks = int( (money - children) / 7 )
                remain = (money - children) % 7
                if chunks < children and remain != 3:
                    return chunks
                else:
                    if remain == 3:
                        if chunks < children-1:
                            return chunks
                        else:
                            if chunks == children - 1:
                                return chunks - 1
                            else:
                                return children - 1
                    else:
                        if chunks == children:
                            return children - 1 if remain != 0 else children
                        else:
                            return children - 1

        
