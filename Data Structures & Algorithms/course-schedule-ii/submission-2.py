class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)
        res = []
        visited, cyclecheck = set(), set()

        def dfs(course):
            if course in cyclecheck:
                return False
            if course in visited:
                return True
            
            cyclecheck.add(course)
            for pre in map[course]:
                if not dfs(pre):
                    return False
            cyclecheck.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res