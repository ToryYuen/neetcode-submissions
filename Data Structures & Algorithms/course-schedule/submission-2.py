class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)

        def dfs(visited, pres):
            if len(pres) == 0:
                return True
            for prerequisite in pres:
                if prerequisite in visited:
                    return False
                visited.add(prerequisite)
                if not dfs(visited, courses[prerequisite]):
                    return False
                courses[prerequisite] = []
                visited.remove(prerequisite)
            return True
            
        for node, pres in courses.items():
            if not dfs(set([node]), pres):
                return False
        return True
