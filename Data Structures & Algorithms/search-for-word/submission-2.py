class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = set()

        def dfs(row, col, index):
            if row >= n or col >= m or row < 0 or col < 0:
                return False

            if board[row][col] != word[index]:
                return False

            if (row, col) in visited:
                return False

            if index == len(word) - 1:
                return True

            visited.add((row, col))

            found = (dfs(row+1, col, index+1) or
            dfs(row-1, col, index+1) or
            dfs(row, col+1, index+1) or
            dfs(row, col-1, index+1))

            visited.remove((row, col))
            return found

        for row in range(n):
            for col in range(m):
                if dfs(row, col, 0):
                    return True
        return False