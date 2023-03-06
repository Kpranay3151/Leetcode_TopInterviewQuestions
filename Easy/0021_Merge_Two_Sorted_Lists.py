# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, la: ListNode, lb: ListNode) -> ListNode:
        d=ListNode()
        tail=d
        while la and lb:
            if la.val < lb.val:
                tail.next=la
                la=la.next
            else:
                tail.next=lb
                lb=lb.next
            tail=tail.next
        if la:
            tail.next=la
        elif lb:
            tail.next=lb
        return d.next
