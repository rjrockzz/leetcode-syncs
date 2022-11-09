class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        # It will keep an adjacency list of the prerequisites needed for a particualr course
        preMap = {i: [] for i in range(numCourses)}
        
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # This will more or less help us with identifying loops in the graph
        visiting = set()
        
        def dfs(crs):
            # If the node has already been visited (looped)
            if crs in visiting:
                return False
            # If we reach the terminal condition, that has no pre-requisites, that's awesome!
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True