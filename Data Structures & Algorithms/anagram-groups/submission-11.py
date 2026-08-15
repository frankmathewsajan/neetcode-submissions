from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            temp = [0]*26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            seen[tuple(temp)].append(s)
        return list(seen.values())
