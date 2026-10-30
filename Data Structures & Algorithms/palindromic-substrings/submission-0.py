class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            cnt = 0

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cnt += 1
                    left -= 1
                    right += 1
                else:
                    break
            return cnt

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i+1)

        return count