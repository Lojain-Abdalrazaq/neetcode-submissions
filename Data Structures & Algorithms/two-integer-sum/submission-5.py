class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store the key-value pairs
        # Time-complexity: O(n)
        # Space-complexity: O(n)
        # Fast lookup for the hashmap -> O(1)
        hashmap_ = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in hashmap_:
                hashmap_[nums[i]] = i # its index
            else:
                return [hashmap_[temp], i]
            
            