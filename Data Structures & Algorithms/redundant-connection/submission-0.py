class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges)+1)]

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour, target, visited):
                        return True

            return False

        for u, v in edges:
            visited = set()
            if dfs(u, v, visited):
                return [u, v]
            else:
                graph[u].append(v)
                graph[v].append(u)  