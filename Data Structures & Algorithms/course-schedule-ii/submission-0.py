class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        res = []
        visited = set()
        circle = set()
        def dfs(crs):
            if crs in circle:
                return False
            if crs in visited:
                return True
            
            visited.add(crs)
            circle.add(crs)
            for neighbor in adj[crs]:
                if not dfs(neighbor):
                    return False
            circle.remove(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res[::-1]