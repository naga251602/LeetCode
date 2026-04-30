# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None

        res, curr = None, None
        ptr = head
        
        while ptr != None:
            if res == None:
                res = ListNode(ptr.val)
                curr = res
            else:
                if curr.val != ptr.val:
                    curr.next = ListNode(ptr.val)
                    curr = curr.next
            ptr = ptr.next
        
        return res