/**
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.
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
    func removeZeroSumSublists(_ head: ListNode?) -> ListNode? {
        var curr: ListNode? = ListNode(0, head);
        var dummy: ListNode? = curr;
        var currSum: Int = 0;
        var hm: [Int: ListNode] = [:]

        while let current = curr {
            currSum += current.val
            hm[currSum] = curr
            curr = current.next
        }

        currSum = 0
        curr = dummy
        while let current = curr {
            currSum += current.val
            current.next = hm[currSum]?.next
            curr = current.next
        }

        return dummy?.next
    }
}