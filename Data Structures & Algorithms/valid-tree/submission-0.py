class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue

                if neighbour in visited:
                    return True

                if dfs(neighbour, node):
                    return True
            return False

        if n == 0:
            return True

        if dfs(0, -1):
            return False

        if len(visited) < n:
            return False
        
        return True