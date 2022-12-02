# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        fake = dummy
        
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                fake.next = head.next
            else:
                fake = fake.next
            head = head.next
        return dummy.next