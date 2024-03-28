"""Lowest Common Ancestor of a Binary Tree

Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of [LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”
"""

from datastructures.binarytree import BinaryTreeNode


def lowestCommonAncestor(root: BinaryTreeNode | None, p: int, q: int) -> int | None:
    if root:
        lca = root.lowestCommonAncestor(p=p, q=q)
        if lca:
            return lca.val
    return None


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# def lowestCommonAncestor(
#     root: TreeNode | None, p: TreeNode, q: TreeNode
# ) -> TreeNode | None:
#     """Solution copied from:
#     https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/3231708/236-solution-with-step-by-step-explanation/
#     """
#     if not root or root == p or root == q:
#         return root

#     l = lowestCommonAncestor(root.left, p, q)
#     r = lowestCommonAncestor(root.right, p, q)

#     if l and r:
#         return root
#     return l or r
