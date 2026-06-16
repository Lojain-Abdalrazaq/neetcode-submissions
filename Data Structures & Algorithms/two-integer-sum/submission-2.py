class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap
        nums_map = {}
        res_list = []
        for i in range(len(nums)):
            target_number = target - nums[i]
            if target_number in nums_map:
                res_list.append(nums_map[target_number])
                res_list.append(i)
                break
            else:
                nums_map[nums[i]] = i
        
        return res_list