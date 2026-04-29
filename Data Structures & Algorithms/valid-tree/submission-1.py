class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)