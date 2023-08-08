# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        res = ListNode(0)
        dummy = res
        carry = 0

        while curr1 or curr2 or carry:
            curr1_val = curr1.val if curr1 else 0
            curr2_val = curr2.val if curr2 else 0

            total = curr1_val + curr2_val + carry
            node_val = total % 10
            carry = total // 10
            dummy.next = ListNode(node_val)

            if curr1: 
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            
            dummy = dummy.next
        return res.next




        
        
        

            
            
        