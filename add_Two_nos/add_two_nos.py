# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_total_and_carry(self, num_1, num_2, carry = 0):
        t = num_1 + num_2 + carry
        carry = int(t/10)
        return (t, carry)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 == None: return l2
        if l2 == None: return l1

        head = None
        curr = None
        carry = 0

        while l1 != None and l2 != None:
            t, carry = self.get_total_and_carry(l1.val, l2.val, carry)
            
            if curr == None:
                curr = ListNode(t%10, None)
                head = curr
            else:
                curr.next = ListNode(t%10, None)
                curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            t, carry = self.get_total_and_carry(l1.val, 0, carry)
            
            curr.next = ListNode(t%10, None)
            curr = curr.next
            l1 = l1.next
        
        while l2 != None:
            t, carry = self.get_total_and_carry(0, l2.val, carry)
            curr.next = ListNode(t%10, None)
            curr = curr.next
            l2 = l2.next

        if carry != 0:
            curr.next = ListNode(carry, None)
            curr = curr.next

        return head