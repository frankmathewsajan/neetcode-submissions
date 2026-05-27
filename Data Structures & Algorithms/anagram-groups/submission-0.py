from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for word in strs:
            s = "".join(sorted(word))
            ana[s] += [word]

        res = []

        for i in ana:
            res.append(ana[i])
        return res       