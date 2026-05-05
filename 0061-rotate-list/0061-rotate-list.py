# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return None

        l = 0
        l_ptr = head

        while l_ptr != None:
            l_ptr = l_ptr.next
            l += 1
        
        k = k%l
        if k == l or k == 0: return head
        
        i, ptr = 0, head

        while i < (l - k - 1):
            ptr = ptr.next
            i += 1
        
        rot, temp = ptr.next, ptr.next
        ptr.next = None

        if k == 1:
            rot.next = head
            return temp
        else:
            while rot.next != None:
                rot = rot.next

            rot.next = head
            return temp
