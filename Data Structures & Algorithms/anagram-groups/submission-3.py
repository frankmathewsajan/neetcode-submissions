
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        def get_id(string):
            temp = [0]*26
            for c in string:
                temp[ord(c) - ord('a')] += 1
            return tuple(temp)
        for s in strs:
            _id = get_id(s)
            if _id in seen:
                seen[_id].append(s)
            else:
                seen[_id] = [s] 

        return list(seen.values())

               