class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        pattern_map = {}
        word_map = {}

        for i in range(len(pattern)):

            char = pattern[i]
            word = s_list[i]

            if char not in pattern_map:
                pattern_map[char] = word
            elif pattern_map[char] != word:
                return False

            if word not in word_map:
                word_map[word] = char
            elif word_map[word] != char:
                return False
        return True
            