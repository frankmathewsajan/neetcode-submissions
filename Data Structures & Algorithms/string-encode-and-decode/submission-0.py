class Solution:

    def encode(self, strs: List[str]) -> str:
        fstr = ""
        for s in strs:
            fstr += s + ":::"
        return fstr
    def decode(self, s: str) -> List[str]:
        strs = s.split(":::")
        return strs[:len(strs) - 1]
