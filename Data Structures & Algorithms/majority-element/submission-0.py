class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = None
        frequency = 0
        for num in nums:
            if n == None:
                n = num
                frequency = 1
            elif num == n:
                frequency += 1
            else:
                frequency -= 1
                if frequency == 0:
                    n = None
        return n