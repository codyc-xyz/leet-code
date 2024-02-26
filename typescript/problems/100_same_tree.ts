// Given the roots of two binary trees p and q, write a function to check if they are the same or not.

// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    
    function dfs(n: TreeNode): (number | null)[] {
        if (n === null) {
            return [null];
        }
        else if (n.left === null && n.right === null) {
            return [n.val];
        }
        const l: number[] | null[] = dfs(n.left);
        const r: number[] | null[] = dfs(n.right);
        return [n.val, ...l, ...r]
    }
    const P = dfs(p);
    const Q = dfs(q);
    return JSON.stringify(P) === JSON.stringify(Q);
};