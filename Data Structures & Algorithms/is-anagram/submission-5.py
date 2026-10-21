class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        if cnt1 != cnt2:
            return False
        return True

