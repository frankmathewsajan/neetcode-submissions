class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x = ord(s[0])
        for i in range(1, len(s)):
            x ^= ord(s[i])
        for i in range(len(t)):
            x ^= ord(t[i])  
        return x == 0      


        