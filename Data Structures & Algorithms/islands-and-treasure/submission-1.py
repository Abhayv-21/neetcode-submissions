from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                if r+dr>=0 and r+dr<rows and c+dc>=0 and c+dc<cols:
                    if grid[r+dr][c+dc] == INF:
                        queue.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = grid[r][c] + 1
                        

        