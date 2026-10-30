# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head: return None
        
        curr, nxt, prev = head, head.next, None
        init = 0
        h = head

        while nxt:
            temp = nxt.next
            nxt.next = curr
            curr.next = temp

            if prev: 
                prev.next = nxt

            prev = curr
            
            curr = curr.next
            
            if init == 0: 
                h = nxt
                
            if curr: nxt = curr.next
            else: break

            init = 1


        return h
            

            

        