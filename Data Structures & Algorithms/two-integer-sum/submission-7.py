class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store the key-value pairs
        # Time-complexity: O(n)
        # Space-complexity: O(n)
        # Fast lookup for the hashmap -> O(1)
        # hashmap_ = {}
        # for i in range(len(nums)):
        #     temp = target - nums[i]
        #     if temp not in hashmap_:
        #         hashmap_[nums[i]] = i # its index
        #     else:
        #         return [hashmap_[temp], i]
        
        # It can be solved using 2-pointers approach:
        # However, we have to sort it, and store the original value with index usign list of tuples
        # [...(value, original_index)]
        # this way cost more time complexity compared to the hashmap way since we are sorting the list before processing
        list_tuples = []
        for i, value in enumerate(nums):
            list_tuples.append((value, i))
        list_tuples.sort()
        ptr1 = 0
        ptr2 = len(nums) - 1
        while ptr1 != ptr2:
            curr_sum = list_tuples[ptr1][0]+list_tuples[ptr2][0]
            if curr_sum > target:
                ptr2 -= 1
            elif curr_sum < target:
                ptr1 += 1
            else:
                return sorted([list_tuples[ptr1][1], list_tuples[ptr2][1]])
                break
