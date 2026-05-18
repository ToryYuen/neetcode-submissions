class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if courses[course] == []:
                return True

            visited.add(course)
            for prerequisite in courses[course]:
                if not dfs(prerequisite):
                    return False
                courses[prerequisite] = []
            visited.remove(course)
            return True
            
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
