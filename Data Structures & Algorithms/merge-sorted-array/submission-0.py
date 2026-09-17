class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # so, since both sorted, we can start from the end to be filled
        last_ptr = n + m -1
        nums1_ptr = m - 1
        nums2_ptr = n - 1

        while nums2_ptr >= 0:
            if nums1_ptr >=0 and nums1[nums1_ptr] >= nums2[nums2_ptr]:
                # filling the zero indexes with the large one
                nums1[last_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[last_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
            
            last_ptr -= 1
