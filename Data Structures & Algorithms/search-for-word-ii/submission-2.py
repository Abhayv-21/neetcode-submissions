class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        visited = set()
        ans = []

        root = TrieNode()

        for word in words:
            node = root

            for ch in word: 
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
            node.word = word

        def dfs(row, col, node):
            if row >= n or col >= m or row < 0 or col < 0:
                return False
            
            if (row, col) in visited:
                return False
            
            if board[row][col] not in node.children:
                return 

            node = node.children[board[row][col]]

            if node.word:
                ans.append(node.word)
                node.word = None

            visited.add((row, col))

            dfs(row+1, col, node)
            dfs(row-1, col, node)
            dfs(row, col+1, node)
            dfs(row, col-1, node)

            visited.remove((row, col))

        for row in range(n):
            for col in range(m):
                if dfs(row, col, root):
                    ans.append(word)

        return ans