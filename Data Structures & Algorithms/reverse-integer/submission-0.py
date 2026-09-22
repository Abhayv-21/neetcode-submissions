class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0 

        if x>0:
            n = str(x)
            n = n[::-1]
            s = ""
            for i in n:
                s += i
            if (-2**31 <= int(s) <= 2**31-1):
                return int(s)
            else:
                return 0
        else:
            n = str(x)
            sign = n[0]
            n = n.replace(sign, "")
            n = n[::-1]
            s= ""
            for i in n:
                s += i
            ans = sign+s
            if (-2**31 <= int(ans) <= 2**31-1):
                return int(ans)
            else:
                return 0