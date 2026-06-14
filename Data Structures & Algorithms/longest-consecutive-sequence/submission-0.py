class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0 
        list_set = set(nums)

        for num in list_set:
            if num-1 not in list_set:
                base_num = num
                lenn=1

                while base_num+1 in list_set:
                    base_num+=1
                    lenn+=1
                
                max_length = max(max_length, lenn)

        return max_length
        