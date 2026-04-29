class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            prereqMap[course].append(preq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereqMap[course] == []:
                return True
            
            visited.add(course)
            for preq in prereqMap[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            prereqMap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True