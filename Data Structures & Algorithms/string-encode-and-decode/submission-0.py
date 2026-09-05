class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            pStart = i
            while s[pStart] != "#":
                pStart += 1
            length = int(s[i:pStart])
            res.append(s[pStart + 1:pStart + 1 + length])
            i = pStart + 1 + length
        return res