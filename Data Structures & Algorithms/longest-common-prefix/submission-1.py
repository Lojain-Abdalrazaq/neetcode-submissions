class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # from its name, the longest common prefix [not siffix or substring]
        # and we will start with the first word  [ the whole word ]
        prefix_str = strs[0] 

        # we will iterate over all the words in the list
        # if the word not equal the current prefix, we will remove the last char from the prefix string
        # until its true
        # and then return the final prefix string

        # Time Complexity: O(N*M^2) -> N: tje number of words on the list
        # M: the number of chars in the first string
        for word in strs[1:]:
            while not word.startswith(prefix_str):
                prefix_str = prefix_str[:-1]
            
        return prefix_str
        