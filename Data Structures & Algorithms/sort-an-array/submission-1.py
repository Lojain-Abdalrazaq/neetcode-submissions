class Solution:
    def sortArray(self, nums):
        # the size of the input array to be sorted
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





    # building the heapify is DONE
    def heapify(self, nums, n, i):
        # nums - array
        # n - how much of the array belongs to the heap
        # i - the node we want to fix

        # we begin by assuming that the index is the largest
        largest =  i
        left = 2 * i + 1
        right = 2 * i + 2

        # left < n - > since maybe the child is not exists in the input array 
        # so, we make sure that it exists usign the n value
        if left < n and nums[left] > nums[largest]:
            largest = left

        if right < n and nums[right] > nums[largest]:
            largest = right
        
        if i != largest:
            # swapping the values 
            nums[i], nums[largest] = nums[largest], nums[i]
            # we check also if the swappign caused any other problems in the buttom
            self.heapify(nums, n, largest)

