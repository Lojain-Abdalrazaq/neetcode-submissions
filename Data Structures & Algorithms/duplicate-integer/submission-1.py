class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        for i in range(len(nums)):
            if nums[i] not in freq_map:
                freq_map[nums[i]] = 1
                print("added to freq_map ")
                print(nums[i])
            else:
                return True
        
        return False
        