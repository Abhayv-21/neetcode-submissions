class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r,c):
            if (r,c) in visited:
                return 0
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if grid[r][c] == 0:
                return 0

            visited.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1) and ((r,c) not in visited):
                    
                    max_area = max(max_area, dfs(r,c))

        return max_area