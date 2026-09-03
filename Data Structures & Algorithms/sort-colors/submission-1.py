class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # this problem has intresting info
        # the array is not general, but the values can be only three values [0,1,2]
        # we have two approaches to solve it:
        # COUNTING
        zero_count = 0
        one_count = 0
        two_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
        
        index = 0
        while zero_count !=0:
            nums[index] = 0 
            zero_count -= 1
            index += 1
        
        while one_count !=0:
            nums[index] = 1
            one_count -= 1
            index += 1
        
        while two_count !=0:
            nums[index] = 2
            two_count -= 1
            index += 1
        


        
        


