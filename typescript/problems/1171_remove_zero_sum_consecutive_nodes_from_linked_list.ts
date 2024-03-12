/**
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)
 */

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeZeroSumSublists(head: ListNode | null): ListNode | null {

    let curr: ListNode | null = new ListNode(0, head);
    let dummy: ListNode | null = curr;
    let hm: Record<number, ListNode> = {}
    let currSum: number = 0;
    while (curr != null) {
        currSum += curr.val
        hm[currSum] = curr
        curr = curr.next
    }

    curr = dummy
    currSum = 0

    while (curr != null) {
        currSum += curr.val
        curr.next = hm[currSum].next
        curr = curr.next
    }
    return dummy.next
    
};