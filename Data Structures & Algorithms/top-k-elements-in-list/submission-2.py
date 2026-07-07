class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        buckets = defaultdict(list)
        for key, val in mp.items():
            buckets[val].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
        
        return res