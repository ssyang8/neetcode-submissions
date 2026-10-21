class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target = strs[0]
        prefix = ""
        for i in range(len(target)):
            prefix = target[:i + 1]
            for word in strs[1:]:
                if not word.startswith(prefix):
                    return prefix[:i]
        
        return prefix
