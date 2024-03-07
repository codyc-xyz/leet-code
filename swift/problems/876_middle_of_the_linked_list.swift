/**
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
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
    func middleNode(_ head: ListNode?) -> ListNode? {
        var fast: ListNode? = head
        var slow: ListNode? = head

        while fast != nil && fast?.next != nil{
            fast = fast?.next?.next
            slow = slow?.next
        }
        return slow
    }
}