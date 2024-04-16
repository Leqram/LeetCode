from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         list_merge = list1+list2
#         return sorted(list_merge)


         
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listnode_class = ListNode()
        listnode = listnode_class

        for val in list1:
            listnode.next = ListNode(val)
            listnode = listnode.next

        for val in list2:
            listnode.next = ListNode(val)
            listnode = listnode.next
        return listnode_class.next

sol = Solution()
list1=[1,2,4]
list2=[1,3,4]
print(sol.mergeTwoLists(list1=list1, list2=list2)) 
        