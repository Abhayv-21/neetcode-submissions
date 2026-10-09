class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(row, col):
            if row >= n or col >= m or row < 0 or col < 0:
                return

            if (row, col) in visited:
                return 
            
            if board[row][col] != "O":
                return
            
            visited.add((row, col))

            for dr, dc in directions:
                nr = row+dr
                nc = col+dc
                if nr >= n or nc >= m or nr < 0 or nc < 0:
                    continue
                dfs(nr, nc) 

        for row in range(n):
            dfs(row, 0)
            dfs(row, m-1)

        for col in range(m):
            dfs(0, col)
            dfs(n-1, col)

        for row in range(n):
            for col in range(m):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"