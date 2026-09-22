class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        def countBits(temp):
            cnt = 0
            for i in temp:
                if i == "1":
                    cnt += 1
            return cnt

        for i in range(n+1):
            curr = bin(i)
            ans.append(countBits(curr))

        return ans