class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for num in st:
            if num - 1 not in st:
                start = num
                cnt = 0
                while start in st:
                    cnt += 1
                    start += 1
                res = max(res, cnt)
        return res
