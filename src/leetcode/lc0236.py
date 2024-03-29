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
