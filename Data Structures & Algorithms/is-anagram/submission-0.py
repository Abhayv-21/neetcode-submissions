class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        dic = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = 1
            else:
                dic[t[i]] += 1

        if seen == dic:
            return True
        else:
            return False