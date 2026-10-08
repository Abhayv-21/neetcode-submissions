class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        ans = []
        curr = []

        def backtrack(start):
            if start == len(s):
                ans.append(curr.copy()) 
                return 

            for end in range(start, len(s)):
                substring = s[start:end+1]

                if substring == substring[::-1]:
                    curr.append(substring)
                    backtrack(end+1)
                    curr.pop()


        backtrack(0)
        return ans