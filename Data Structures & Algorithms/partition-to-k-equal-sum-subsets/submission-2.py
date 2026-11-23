class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        target = sum(nums) // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        n = len(nums)
        used = [False] * n
        def dfs(start, k, total):
            if k == 0:
                return True
            if total == target:
                return dfs(0, k - 1, 0)
            for i in range(start, n):
                if used[i] or total + nums[i] > target:
                    continue
                if i >= 1 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                if dfs(i + 1, k, total + nums[i]):
                    return True
                used[i] = False
            return False
        return dfs(0, k, 0)
            

