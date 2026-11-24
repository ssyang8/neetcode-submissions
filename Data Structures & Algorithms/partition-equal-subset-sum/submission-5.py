class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        n = len(nums)
        cache = {}
        def dfs(i, rem):
            if rem < 0:
                return False
            if i >= n and rem > 0:
                return False
            if rem == 0:
                return True
            if (i, rem) in cache:
                return cache[(i, rem)]
            
            for j in range(i, n):
                if dfs(j + 1, rem - nums[i]):
                    cache[(i, rem)] = True
                    return cache[(i, rem)]
            cache[(i, rem)] = False
            return cache[(i, rem)]
        return dfs(0, target)
