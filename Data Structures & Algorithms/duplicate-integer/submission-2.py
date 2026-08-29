class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap_ = {}
        for i in range(len(nums)):
            if nums[i] in hashmap_:
                return True
            else:
                hashmap_[nums[i]] = 1
        
        return False