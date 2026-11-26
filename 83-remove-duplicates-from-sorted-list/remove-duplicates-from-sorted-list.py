# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        tail = head
        while tail and tail.next:
            if tail.val == tail.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next

        return head
        