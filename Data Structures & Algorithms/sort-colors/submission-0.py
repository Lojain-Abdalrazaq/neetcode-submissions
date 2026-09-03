class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # this problem has intresting info
        # the array is not general, but the values can be only three values [0,1,2]
        # we have two approaches to solve it:
        # COUNTING
        count0 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1


        i = 0

        for _ in range(count0):
            nums[i] = 0
            i += 1

        for _ in range(count1):
            nums[i] = 1
            i += 1

        for _ in range(count2):
            nums[i] = 2
            i += 1



        # Three Pointers: