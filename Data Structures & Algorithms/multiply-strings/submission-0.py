class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1==0 or num2==0:
            return 0

        c1 = int(num1)
        c2 = int(num2)

        c = c1*c2

        n = str(c)

        return n