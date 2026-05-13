# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr_1, ptr_2 = l1, l2
        res, curr = None, None
        c = 0

        while ptr_1 != None and ptr_2 != None:
            data = ptr_1.val + ptr_2.val + c
            if res == None:
                res = ListNode(data%10)
                curr = res
            else:
                curr.next = ListNode(data%10)
                curr = curr.next
            c = data // 10
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
        
        while ptr_1 != None:
            data = ptr_1.val + c
            if res == None:
                res = ListNode(data%10)
                curr = res
            else:
                curr.next = ListNode(data%10)
                curr = curr.next
            c = data // 10
            ptr_1 = ptr_1.next

        while ptr_2 != None:
            data = ptr_2.val + c
            if res == None:
                res = ListNode(data%10)
                curr = res
            else:
                curr.next = ListNode(data%10)
                curr = curr.next
            c = data // 10
            ptr_2 = ptr_2.next
        
        if c != 0:
            curr.next = ListNode(1)
            curr = curr.next
        return res
