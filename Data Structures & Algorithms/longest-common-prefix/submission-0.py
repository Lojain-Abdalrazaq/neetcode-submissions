class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # from its name, the longest common prefix [not siffix or substring]
        # and we will start with the first word  [ the whole word ]
        prefix_str = strs[0] 

        for word in strs[1:]:
            while not word.startswith(prefix_str):
                prefix_str = prefix_str[:-1]
            
        return prefix_str
        