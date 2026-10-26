class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
            
        q = deque()
        for i, crs in enumerate(indegree):
            if crs == 0:
                q.append(i)
        
        taken = 0
        while q:
            crs = q.popleft()
            taken += 1
            
            for neighbor in adj[crs]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return True if taken == numCourses else False
