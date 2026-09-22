class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a==0:
            return b
        if b == 0:
            return a 

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF 

        while b!=0:
            sum_without_carry = (a ^ b)
            carry = (a & b) << 1

            a = sum_without_carry & mask
            b = carry & mask
        
        if a <= max_int:
            return a

        return ~(a ^ mask)