/**
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
**/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeInBetween(_ list1: ListNode?, _ a: Int, _ b: Int, _ list2: ListNode?) -> ListNode? {
        var head1: ListNode? = ListNode(0, list1)
        var head2: ListNode? = ListNode(0, list2)
        var tail1: ListNode? = head1
        var tail2: ListNode? = head2
        var B: Int = b
        var A: Int = a
        while B >= 0 {
            tail1 = tail1?.next
            B -= 1
        }

        while tail2?.next != nil {
            tail2 = tail2?.next
        }
        var curr: ListNode? = head1
        while A > 0 {
            curr = curr?.next
            A -= 1
        }
        curr?.next = head2?.next
        tail2?.next = tail1?.next
        return head1?.next
    }

    
}