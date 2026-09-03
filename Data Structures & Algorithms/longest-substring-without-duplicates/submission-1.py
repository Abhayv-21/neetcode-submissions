class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        cnt = 0
        max_cnt = 0
        for i in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                cnt += 1
                right += 1
                max_cnt = max(cnt, max_cnt)
            elif s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                    cnt -= 1
                seen.add(s[right])
                cnt += 1
                right += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt
