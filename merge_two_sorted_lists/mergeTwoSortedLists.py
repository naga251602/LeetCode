# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None: return list2
        if list2 == None: return list1

        temp = None
        head = None

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                if temp == None: 
                    temp = ListNode(list1.val, None)
                    head = temp
                else:
                    curr = ListNode(list1.val, None)
                    temp.next = curr
                    temp = curr
                list1 = list1.next
            else:
                if temp == None: 
                    temp = ListNode(list2.val, None)
                    head = temp
                else:
                    curr = ListNode(list2.val, None)
                    temp.next = curr
                    temp = curr
                list2 = list2.next
            
            
        
        while list1 != None:
            curr = ListNode(list1.val, None)
            temp.next = curr
            temp = curr
            list1 = list1.next
            
            
        
        while list2 != None:
            curr = ListNode(list2.val, None)
            temp.next = curr
            temp = curr
            list2 = list2.next
            

        return head
        