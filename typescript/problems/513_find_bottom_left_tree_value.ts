// Given the root of a binary tree, return the leftmost value in the last row of the tree.

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

function findBottomLeftValue(root: TreeNode | null): number {
    
    let dq: TreeNode[] = [root];
    let ans: number;
    while (dq.length > 0) {
        let curr: TreeNode = dq.shift();
        ans = curr.val
        if (curr.right !== null) {
            dq.push(curr.right)
        }
        if (curr.left !== null) {
            dq.push(curr.left)
        }
    }
    return ans

};