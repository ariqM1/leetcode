# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        
        # reverse second half
        curr = mid
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # now combine first half with reversed second half
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2


        

