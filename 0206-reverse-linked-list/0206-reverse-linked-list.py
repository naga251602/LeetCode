# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None

        ptr, n = head, None

        while ptr != None:
            temp = ptr.next 
            ptr.next = n
            n = ptr
            ptr = temp

        return n


            