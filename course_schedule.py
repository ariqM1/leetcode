class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True

            visited.add(course)
            for req in preMap[course]:
                if not dfs(req): 
                    return False

            visited.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
