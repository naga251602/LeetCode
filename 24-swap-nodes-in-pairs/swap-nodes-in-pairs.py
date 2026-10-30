# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head: return None
        
        curr, nxt, prev = head, head.next, None

        while nxt:
            # swap logic
            temp = nxt.next
            nxt.next = curr
            curr.next = temp

            # checking if this is the first update
            if prev: 
                # if no then its the second chain update the previous node 
                prev.next = nxt
            else:
                # first update so next node becomes the first
                head = nxt

            prev = curr
            curr = curr.next
            
            # check if we have atleast 2 nodes to perform the operation
            if curr: nxt = curr.next
            else: break

        return head
            

            

        