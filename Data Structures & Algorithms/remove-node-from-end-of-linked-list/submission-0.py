# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        # or temp.next = head
        fast = temp
        slow = temp
        nums = n

        # to move it n nodes away from the slow pointer
        while nums>0:
            fast = fast.next
            nums -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return temp.next
  