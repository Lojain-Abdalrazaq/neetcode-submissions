class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in s_map:
                s_map[s_char] = t_char
            elif s_map[s_char] != t_char:
                return False
            
            if t_char not in t_map:
                t_map[t_char] = s_char
            elif t_map[t_char] != s_char:
                return False
        
        return True
        