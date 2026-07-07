class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            res.append(str(len(st)))
            res.append('#')
            res.append(st)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num_str = ''
            while s[i] != '#':
                num_str += s[i]
                i += 1
            num = int(num_str)
            i += 1
            res.append(s[i:i + num])
            i += num
        return res


