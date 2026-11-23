class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(st: str) -> bool:
            i, j = 0, len(st) - 1
            while i < j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            return True

        res = []
        path = []
        n = len(s)

        def dfs(start: int):
            # 1. 整根字符串刚好全部分割完毕，收集当前切分方案
            if start == n:
                res.append(path[:])
                return

            # 2. 枚举这一刀的结束位置 i，切出子串 s[start : i + 1]
            for i in range(start, n):
                sub = s[start : i + 1]
                # 剪枝：只有当前切出来的这一段是回文串，才继续往下切
                if not isPalindrome(sub):
                    continue
                path.append(sub)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
