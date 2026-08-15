class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False         
        C = [0]*26
        for i in range(len(s)):
            C[ord(s[i]) - ord('a')] += 1
            C[ord(t[i]) - ord('a')] -= 1   
        return all(c == 0 for c in C)       
            


        