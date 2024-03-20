/**

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

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

function mergeInBetween(list1: ListNode | null, a: number, b: number, list2: ListNode | null): ListNode | null {

    let head1: ListNode | null = new ListNode(0, list1);
    let tail1: ListNode | null = head1;

    while (b >= 0) {
        tail1 = tail1.next
        b -= 1
    }
    let tail2: ListNode | null = new ListNode(0, list2)
    let head2: ListNode | null = tail2

    while (tail2.next) {
        tail2 = tail2.next
    }

    let curr: ListNode | null = head1;
    while (a > 0) {
        curr = curr.next
        a -= 1
    }
    curr.next = head2.next
    tail2.next = tail1.next

    return head1.next

    
};