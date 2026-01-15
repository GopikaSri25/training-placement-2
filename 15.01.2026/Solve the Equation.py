class Solution(object):
    def solveEquation(self, equation):
        def parse_side(side):
            coef = 0  
            const = 0  
            i = 0
            n = len(side)
            
            while i < n:
                if side[i] == '+' or side[i] == '-':
                    sign = 1 if side[i] == '+' else -1
                    i += 1
                else:
                    sign = 1
                
                if i < n and side[i] == 'x':
                    coef += sign * 1
                    i += 1
                else:
                    num = 0
                    while i < n and side[i].isdigit():
                        num = num * 10 + int(side[i])
                        i += 1
                    if i < n and side[i] == 'x':
                        coef += sign * num
                        i += 1
                    else:
                        const += sign * num
            
            return coef, const
        
        lhs, rhs = equation.split('=')
        
        lhs_coef, lhs_const = parse_side(lhs)
        rhs_coef, rhs_const = parse_side(rhs)
        
        coef = lhs_coef - rhs_coef
        const = rhs_const - lhs_const
        
        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return "x=" + str(const // coef)
