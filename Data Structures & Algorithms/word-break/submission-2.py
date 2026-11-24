class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st = set(wordDict)
        cache = {}
        n = len(s)
        def dfs(i):
            if i == n:
                return True
            if i in cache:
                return cache[i]
            for j in range(i + 1, n + 1):
                if s[i:j] in st and dfs(j):
                    cache[i] = True
                    return True
            cache[i] = False
            return cache[i]
        
        return dfs(0)


