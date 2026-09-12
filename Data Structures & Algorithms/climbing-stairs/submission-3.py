class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(n):
            if n==1:
                memo[1] = 1
                return 1
            elif n==2:
                memo[2] = 2
                return 2

            else:
                if (n-1) not in memo:
                    memo[n-1] = climb(n-1)
                if (n-2) not in memo:
                    memo[n-2] = climb(n-2)
                return memo[n-1] + memo[n-2]

        return climb(n)