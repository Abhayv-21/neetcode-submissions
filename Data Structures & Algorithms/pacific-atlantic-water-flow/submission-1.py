class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set() 
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = []

        def dfs(row, col, reachable):
            if row >= n or col >= m or row < 0 or col < 0:
                return

            if (row, col) in reachable:
                return

            reachable.add((row, col))

            for dr, dc in directions: 
                nr = row+dr
                nc = col+dc
                
                if nr >= n or nc >= m or nr < 0 or nc < 0:
                    continue

                if heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, reachable)

        for row in range(n):
            dfs(row, 0, pacific)
            dfs(row, m-1, atlantic)

        for col in range(m):
            dfs(0, col, pacific) 
            dfs(n-1, col, atlantic)
        ans = list(pacific & atlantic)
        return ans