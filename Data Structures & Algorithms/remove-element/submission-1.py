class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # In this question, I am planning to use the Two-pointers approach
        # since the order not important, we can use the swapping techneque
        right_ptr = len(nums)-1
        left_ptr = 0

        while left_ptr <= right_ptr:
            if nums[left_ptr] == val:
                while left_ptr <= right_ptr:
                    if nums[right_ptr]!=val:
                        # swap
                        nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                        break
                    else:
                        right_ptr -= 1 # to the left one step
            left_ptr += 1

        return right_ptr + 1