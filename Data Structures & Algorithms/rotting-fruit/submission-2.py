from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue:
            size = len(queue)
            rotted = False

            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if r+dr>=0 and r+dr<rows and c+dc>=0 and c+dc<cols:
                        if grid[r+dr][c+dc] == 1:
                            queue.append((r+dr, c+dc))
                            grid[r+dr][c+dc] = 2
                            rotted = True
            if rotted:
                time += 1

        for r in range(rows):
            for c in range(cols):
                  if grid[r][c] == 1:
                    return -1
        return time     