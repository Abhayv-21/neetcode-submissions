class Solution:
    def reverseBits(self, n: int) -> int:
        s = format(n, '032b')

        s = s[::-1]
        num = 0
        for i in s:
            num = num*2 + (ord(i)-ord('0'))

        return num