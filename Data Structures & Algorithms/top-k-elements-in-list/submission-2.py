class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] in nums_map:
                nums_map[nums[i]] +=1
            else:
                nums_map[nums[i]] = 1
        
        # sort the map according to the values
        # return first k elements
        sorted_list = sorted(nums_map.items(), key = lambda x : x[1], reverse = True)
        print(sorted_list)
        result = []
        for nums,freq in sorted_list:
            result.append(nums)

        return result[:k]
                