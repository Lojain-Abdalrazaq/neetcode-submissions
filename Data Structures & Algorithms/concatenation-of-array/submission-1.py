class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # time complexity = O(N)
        # space complexity = O(2*n) [Such that n is the input array lengh] = O(n)
        # input_len = len(nums)
        # ans = [0]*input_len*2
        # for i in range(input_len):
        #     ans[i] = nums[i]
        #     ans[i+input_len] = nums[i]

        # return ans
        return nums+nums
        