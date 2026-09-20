class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        seen = []

        def happy(n, seen): 
            curr = 0
            digits = [int(digit) for digit in str(n)]

            for i in digits:
                curr += i**2

            if curr==1:
                return True
            else:
                if curr in seen:  
                    return False
                else:
                    seen.append(curr)
                    return happy(curr, seen)  


        return happy(n, seen)