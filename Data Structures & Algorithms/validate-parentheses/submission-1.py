class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                stack.append(i)

            else:
                if len(stack) == 0:
                    return False
                elif pairs[stack[-1]] != i:
                    return False
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False