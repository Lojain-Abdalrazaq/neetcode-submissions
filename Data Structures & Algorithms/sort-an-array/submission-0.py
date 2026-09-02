class Solution:
    def sortArray(self, nums):
        n = len(nums)

        # 1. Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # 2. Move the maximum element to the end
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]

            # 3. Fix the remaining heap
            self.heapify(nums, i, 0)

        return nums

    def heapify(self, nums, n, i):
        largest = i

        left = 2 * i + 1
        right = 2 * i + 2

        # Is left child larger?
        if left < n and nums[left] > nums[largest]:
            largest = left

        # Is right child larger?
        if right < n and nums[right] > nums[largest]:
            largest = right

        # If the current node isn't the largest, swap
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]

            # The problem may have moved down
            self.heapify(nums, n, largest)