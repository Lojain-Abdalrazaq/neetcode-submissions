class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        input_len = len(nums)
        ans = [0]*input_len*2
        for i in range(input_len):
            ans[i] = nums[i]
            ans[i+input_len] = nums[i]

        return ans
        