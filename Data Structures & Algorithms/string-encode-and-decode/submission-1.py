class Solution:

    def encode(self, strs: List[str]) -> str:
        fstr = ""
        for s in strs:
            fstr += s + "8"
        return fstr
    def decode(self, s: str) -> List[str]:
        strs = s.split("8")
        return strs[:len(strs) - 1]
