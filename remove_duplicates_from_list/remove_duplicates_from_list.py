# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head

        ptr = head
        curr = ptr
        temp = curr    
        ptr = ptr.next

        while ptr != None:
            if curr.val != ptr.val:
                curr.next = ptr
                curr = curr.next
            ptr = ptr.next
            curr.next = None

        return temp

        