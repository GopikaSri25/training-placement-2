class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack
