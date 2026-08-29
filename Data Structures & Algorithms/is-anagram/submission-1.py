class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        if len(s) != len(t):
            return False

        # preparing the first hashmap key-value for the 1st string
        for i in range(len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in hash_map:
                return False
            else:
                if hash_map[t[j]] < 1:
                    return False
                else:
                    hash_map[t[j]] -= 1

        return True