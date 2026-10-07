class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(opened, closed, curr):
            if opened == n and closed == n:
                ans.append("".join(curr))
                return

            if opened < n:
                curr.append("(")
                opened += 1
                backtrack(opened, closed, curr)
                curr.pop()
                opened -=1 
            if closed < opened :
                curr.append(")")
                closed += 1
                backtrack(opened, closed, curr)
                curr.pop()
                closed -= 1

        opened = 0
        closed = 0
        curr = []
        backtrack(opened, closed, curr)
        return ans