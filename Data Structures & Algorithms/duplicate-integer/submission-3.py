class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # BOTH solutions have early check and return the result
        # without the need to get over all the input list
        # Using Hashmap
        # hashmap_ = {}
        # for i in range(len(nums)):
        #     if nums[i] in hashmap_:
        #         return True
        #     else:
        #         hashmap_[nums[i]] = 1
        # return False

        # Using Set
        out_set = set()
        for num in nums:
            if num in out_set:
                return True
            out_set.add(num)

        return False