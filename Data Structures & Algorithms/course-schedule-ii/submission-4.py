class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we create a map to store the adjacency list for all the courses
        map = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)
        
        # we create a cycle set to check if the path is cyclic and a visited set to keep track of the courses already visited by the dfs
        visited, cycle = set(),set()
        res = []
        # now we create the dfs function
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in map[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        # now we call the dfs from each node in the graph
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res