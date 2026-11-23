class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def dfs(start, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, n):
                path.append(nums[i])
                dfs(i, total + nums[i])
                path.pop()
        dfs(0, 0)
        return res