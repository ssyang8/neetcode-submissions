class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        path = []
        def dfs(start):
            res.append(path[:])

            for i in range(start, n):
                if i >= 1 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
                used[i] = False
        nums.sort()
        dfs(0)
        
        return res
