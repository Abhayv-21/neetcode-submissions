class Solution:
    def hammingWeight(self, n: int) -> int:
        curr = bin(n)
        temp = str(curr)
        cnt = 0

        for i in temp:
            if i=="1":
                cnt += 1
            
        return cnt