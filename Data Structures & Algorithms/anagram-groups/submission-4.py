class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution # 1:
        # the first approach using sorting + hashmap:
        # Space Complexity: 
        # Time Complexity: Sorting for a word -> O(nlog n)
        # for m words -> O(m*nlogn)
        # Space Complexity: key - value [ list ] -> O(n*m)
        hash_map = {}
        list_result = []

        for word in strs:
            if ''.join(sorted(word)) in hash_map:
                hash_map[''.join(sorted(word))].append(word)
            else:
                hash_map[''.join(sorted(word))] = [word]
        
        for key in hash_map:
            list_result.append(hash_map[key])
        
        return list_result

        
        # Solution # 2:
        # instead of sort the word and use it as key, we use array of size 26
        # as the key of the hashmap     