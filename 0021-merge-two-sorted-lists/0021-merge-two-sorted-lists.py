# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None: return None
        if list1 == None: return list2
        if list2 == None: return list1

        res, curr = None, None

        ptr_1, ptr_2 = list1, list2

        while ptr_1 != None and ptr_2 != None:
            if ptr_1.val <= ptr_2.val:
                if res == None:
                    res =  ListNode(ptr_1.val)
                    curr = res
                else:
                    curr.next = ListNode(ptr_1.val)
                    curr = curr.next
                ptr_1 = ptr_1.next
            else:
                if res == None:
                    res =  ListNode(ptr_2.val)
                    curr = res
                else:
                    curr.next = ListNode(ptr_2.val)
                    curr = curr.next               
                ptr_2 = ptr_2.next

        while ptr_1 != None:
            if res == None:
                res =  ListNode(ptr_1.val)
                curr = res
            else:
                curr.next = ListNode(ptr_1.val)
                curr = curr.next
            ptr_1 = ptr_1.next
        
        while ptr_2 != None:
            if res == None:
                res =  ListNode(ptr_2.val)
                curr = res
            else:
                curr.next = ListNode(ptr_2.val)
                curr = curr.next
            ptr_2 = ptr_2.next
        return res