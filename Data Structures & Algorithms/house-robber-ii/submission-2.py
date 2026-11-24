class Solution:
    def rob(self, nums: List[int]) -> int:
        # 边界情况：只有 1 间房时，切片 nums[:-1] 和 nums[1:] 都会变空，必须单独返回
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr: List[int]) -> int:
            n = len(arr)
            memo = {}

            def dfs(i: int) -> int:
                if i >= n:
                    return 0
                if i in memo:
                    return memo[i]

                memo[i] = max(dfs(i + 1), arr[i] + dfs(i + 2))
                return memo[i]

            return dfs(0)

        # 情况 1：放弃最后一间 nums[:-1] vs 情况 2：放弃第一间 nums[1:]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
