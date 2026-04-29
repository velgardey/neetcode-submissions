class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # an empty edge list is also a valid tree:
        if not n:
            return True
        
        # we create an adj map to store the nodes as key and neighbours as values
        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # we create a visited set to keep track of the nodes visited
        visited = set()
        # now we define the dfs function to explore each node
        def dfs(node, prev): # prev is added so that the node does not go to the previous node and create a false cyclic check
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