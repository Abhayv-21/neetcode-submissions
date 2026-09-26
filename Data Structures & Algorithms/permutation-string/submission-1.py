class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq = {}
        window = {}

        for i in range(len(s1)):
            if s1[i] not in freq:
                freq[s1[i]] = 0
            freq[s1[i]] += 1

        for i in range(len(s1)):
            if s2[i] not in window:
                window[s2[i]] = 0
            window[s2[i]] += 1

        if window == freq:
            return True
        
        slow = 0
        fast = len(s1)

        while fast<len(s2):
            window[s2[slow]] -= 1
            if window[s2[slow]] == 0:
                window.pop(s2[slow])

            if s2[fast] not in window: 
                window[s2[fast]] = 0

            window[s2[fast]] += 1

            slow += 1
            fast += 1

            if window == freq:
                return True

        return False