class Solution:

    def encode(self, strs: List[str]) -> str:
        fstr = ""
        for s in strs:
            fstr += f"{len(s)}#{s}"
        return fstr
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find('#', i)
            l = int(s[i:j])
            
            res.append(s[j+1:j+1+l])

            i = j + l + 1
        return res    

