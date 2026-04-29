class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we make a map to store the courses and their prerequisites
        # since we need an array as the value in key : value, we need to initialize it
        map = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            map[course].append(pre)

        # we make a set to store the courses visited during the present dfs search
        visited = set()

        def dfs(course):
            # we check if the course results in a cycle
            if course in visited:
                return False
            # we check if the end base case course is reached
            if map[course]==[]:
                return True
            # we add the current course to the set
            visited.add(course)
            for pre in map[course]:
                if not dfs(pre):
                    return False # means the courses cannot be completed
            visited.remove(course)
            map[course] = []
            return True 

        # now we have to call this dfs from each course in numCourses
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True 
