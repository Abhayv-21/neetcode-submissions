class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0

        # curr = x

        # for i in range(1, n):
        #     curr *= x

        return x**n