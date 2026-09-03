class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visited = {}
        left = 0
        right = 0
        max_len = 0
        for i in range(len(s)):
            if s[right] not in visited:
                visited[s[right]] = 1
            else:
                visited[s[right]] += 1
            
            window = right - left + 1
            max_freq = max(visited.values())
            if window - max_freq > k:
                visited[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

            right += 1
        return max_len