class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        M = 0
        for r in range(len(s)):
            while s[r] in char_set:   
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            M = max(M, r - l + 1)
        return M
