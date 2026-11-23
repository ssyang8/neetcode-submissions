class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        def dfs(start):
            res.append(path[:])
            
            for i in range(start, n):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return res
