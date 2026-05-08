# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        st = set()
        ptr = head

        while ptr != None:
            if ptr in st: return True
            st.add(ptr)
            ptr = ptr.next
        
        return False

