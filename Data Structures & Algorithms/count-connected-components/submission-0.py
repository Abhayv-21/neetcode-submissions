class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        visited = set()
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                cnt += 1
                dfs(node)

        return cnt