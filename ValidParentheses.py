"""
Well-known EZ problem.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if (
                        (top == '(' and char != ')')
                        or (top == '{' and char != '}')
                        or (top == '[' and char != ']')
                ):
                    return False

        return len(stack) == 0
