class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False         
        S, T = [0]*26, [0]*26
        for i in range(len(s)):
            S[ord(s[i]) - ord('a')] += 1
            T[ord(t[i]) - ord('a')] += 1
        print(S,"\n",T)    
        for i in range(26):
            if S[i] != T[i]:
                return False
        return True        
            


        