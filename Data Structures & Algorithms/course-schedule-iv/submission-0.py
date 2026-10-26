class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)

        def dfs(crs, target, visited):
            if crs == target:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for neighbor in adj[crs]:
                if dfs(neighbor, target, visited):
                    return True

            return False

        res = []
        for pre, crs in queries:
            res.append(dfs(pre, crs, set()))
        return res