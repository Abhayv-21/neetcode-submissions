class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r,c):
            if (r,c) in visited:
                return 
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            if grid[r][c] == "0":
                return

            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1") and ((r,c) not in visited):
                    dfs(r,c)
                    ans += 1

        return ans