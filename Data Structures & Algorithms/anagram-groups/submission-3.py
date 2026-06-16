class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        list_result = []

        for i in range(len(strs)):
            sorted_string = sorted(strs[i]) # will be as a list
            joined_string = ''.join(sorted_string)
            if joined_string not in hash_map:
                hash_map[joined_string] = [strs[i]]
            else:
                hash_map[joined_string].append(strs[i])

        
        for key in hash_map:
            list_result.append(hash_map[key])
        
        return list_result