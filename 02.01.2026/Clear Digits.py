class Solution(object):
    def clearDigits(self, s):
        stack = []
        for char in s:
            if not char.isdigit():
                stack.append(char)
            else:
                if stack:
                    stack.pop()

        return "".join(stack)
