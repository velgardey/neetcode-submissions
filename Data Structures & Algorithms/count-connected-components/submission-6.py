class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we create a adj list for storing the nodes and its neighbours
        adj = {i:[] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(node)
                    dfs(nei)


        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res
