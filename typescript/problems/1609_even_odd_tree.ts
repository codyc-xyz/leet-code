/**
The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
 */

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isEvenOddTree(root: TreeNode | null): boolean {
    
    let dq: TreeNode[] = [root]
    let level: number = 0;
    while (dq.length > 0) {
        let lenDq: number = dq.length;
        let prev: number;
        if (level % 2 === 1) {
            prev = Infinity
        }
        else {
            prev = -Infinity
        }
        while (lenDq > 0) {
            const curr: TreeNode = dq.shift();
            if (level % 2 === 1 && (curr.val % 2 === 1 || prev <= curr.val)) {
                return false
            }
            else if (level % 2 === 0 && (curr.val % 2 === 0 || prev >= curr.val)) {
                return false
            }
            if (curr.left) {
                dq.push(curr.left)
            }
            if (curr.right) {
                dq.push(curr.right)
            }
            lenDq -= 1
            prev = curr.val
        }
        level++
    }
    return true
};