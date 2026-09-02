class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach number 1: Using hashmap
        # time and space complexity: O(n)
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] +=1 
                # checking the freq
            else:
                freq_map[num] = 1
                
            if freq_map[num] > len(nums) // 2:
                    return num