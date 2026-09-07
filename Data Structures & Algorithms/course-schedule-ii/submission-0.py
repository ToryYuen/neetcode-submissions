class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)        

        # visited = course has been added
        # visiting = added to cycle
        # unvisted = course not added to putput or cycle
        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prerequisite in courses[course]:
                if dfs(prerequisite) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                    return []
        return output