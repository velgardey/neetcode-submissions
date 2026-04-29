class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we make the parent array where i node has par[i] parent 
        parent = [i for i in range(len(edges) + 1)]  # since no. of edges = n and no. or nodes from 0 to n
        rank = [1] * (len(edges) + 1) # creates an array where the rank of the root parent is stored i.e. the height

        # we create a find func to find the root parent of a node
        def find(node):
            p = parent[node]
            while p != parent[p]: # check if the parent node is the root one as it is a parent to itself
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p # returns the root parent
        
        # we create a union func that links the nodes and checks for any cycles
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            # check if the nodes have the same parent i.e. a cycle is detected
            if parent1 == parent2:
                return False
            
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1 # add the smaller tree as a child to the larger tree
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        # check for each egde
        for node1, node2 in edges:
            if not union(node1, node2): # if union returns False that means a cycle as been detected for that pair of nodes
                return [node1, node2]