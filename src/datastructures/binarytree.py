"""Definition for a binary tree node."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class BinaryTreeNode:
    data: int
    left: BinaryTreeNode | None = None
    right: BinaryTreeNode | None = None

    def __repr__(self) -> str:
        return f"val: {self.data}, left: {self.left}, right: {self.right}"

    def __str__(self):
        return f"<{self.data}, {self.left}, {self.right}>"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, BinaryTreeNode)
            and self.data == other.data
            and self.left == other.left
            and self.right == other.right
        )

    @classmethod
    def from_list_long_iter(cls, nums: list[int | None]) -> BinaryTreeNode | None:
        """Note: short vs long representation:
        -   Short form: [1, None, 2, 3]
        -   Long form: [1, None, 2, None, None, 3]
        This only works if `nums` is in long form.
        If `nums` is in short form, transform it using `transform_short_to_long`.
        """
        if not nums or not nums[0]:
            return None

        def _inner(index: int = 0) -> BinaryTreeNode | None:
            if index >= len(nums) or not nums[index]:
                return None
            node = BinaryTreeNode(data=nums[index])  # type: ignore
            node.left = _inner(index=2 * index + 1)
            node.right = _inner(index=2 * index + 2)
            return node

        return _inner()

    @classmethod
    def from_list_long_recur(cls, nums: list[int | None]) -> BinaryTreeNode | None:
        """Note: short vs long representation:
        -   Short form: [1, None, 2, 3]
        -   Long form: [1, None, 2, None, None, 3]
        This only works if `nums` is in long form.
        If `nums` is in short form, transform it using `transform_short_to_long`.
        """
        if not nums or not nums[0]:
            return None

        root = BinaryTreeNode(nums[0])
        root.left = cls.from_list_long_recur(
            nums=[n for (i, n) in enumerate(nums) if i % 2 == 1]
        )
        root.right = cls.from_list_long_recur(
            nums=[n for (i, n) in enumerate(nums) if i != 0 and i % 2 == 0]
        )
        return root

    @classmethod
    def transform_short_to_long(cls, short: list[int | None]) -> list[int | None]:
        """Note: short vs long representation:
        -   Short form: [1, None, 2, 3]
        -   Long form: [1, None, 2, None, None, 3]
        If your list is in short form, use this to transform it to long form.
        """
        long = short.copy()
        i = 0
        while i < len(long):
            if not long[i]:
                if 2 * i + 1 < len(long):
                    long.insert(2 * i + 1, None)
                if 2 * i + 2 < len(long):
                    long.insert(2 * i + 2, None)
            i += 1
        return long

    def inorderTraversal_recur(self) -> list[int]:
        if not self:
            return []
        result_left = self.left.inorderTraversal_recur() if self.left else []
        result_right = self.right.inorderTraversal_recur() if self.right else []
        return result_left + [self.data] + result_right

    def preorderTraversal_recur(self) -> list[int]:
        if not self:
            return []
        result_left = self.left.preorderTraversal_recur() if self.left else []
        result_right = self.right.preorderTraversal_recur() if self.right else []
        return [self.data] + result_left + result_right

    def postorderTraversal_recur(self) -> list[int]:
        if not self:
            return []
        result_left = self.left.postorderTraversal_recur() if self.left else []
        result_right = self.right.postorderTraversal_recur() if self.right else []
        return result_left + result_right + [self.data]

    def invert(self):
        """Invert tree in place."""
        if not self:
            return self

        if self.left and self.right:
            (self.left, self.right) = (self.right, self.left)
        elif self.left:
            (self.left, self.right) = (None, self.left)
        elif self.right:
            (self.left, self.right) = (self.right, None)
        else:
            return self

        if self.left:
            self.left.invert()
        if self.right:
            self.right.invert()

    def rightSideView(self) -> list[int]:
        if not self:
            return []
        rsv: list[int] = []
        queue: deque[BinaryTreeNode] = deque()
        queue.append(self)
        while queue:
            rsv.append(queue[0].data)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return rsv

    def lowestCommonAncestor(self, p: int, q: int) -> BinaryTreeNode | None:
        """Solution copied from:
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/3231708/236-solution-with-step-by-step-explanation/
        """
        if not self or self.data == p or self.data == q:
            return self

        ancestor_left = self.left.lowestCommonAncestor(p, q) if self.left else None
        ancestor_right = self.right.lowestCommonAncestor(p, q) if self.right else None

        if ancestor_left and ancestor_right:
            return self
        return ancestor_left or ancestor_right

    def maxDepth(self) -> int:
        """Maximum depth of the binary tree.
        Time complexity: O(n), space complexity: Ω(log(n)) ∩ O(n), where `n` is the number of nodes.
        Space complexity is due to recursion from the depth of tree.
        """
        if not self:
            return 0
        depth_left = self.left.maxDepth() if self.left else 0
        depth_right = self.right.maxDepth() if self.right else 0
        return 1 + max(depth_left, depth_right)

    def diameter_naive(self) -> int:
        """Recursive relation:
            diameter = max{depth_max(left) + depth_max(right), diameter(left), diameter(right)}.
        Time complexity: O(n^2), space complexity: Ω(log(n)) ∩ O(n), where `n` is the number of nodes.
        Space complexity is due to recursion from the depth of tree.
        This is suboptimal as we visit the nodes multiple times (for the maxDepth).
        """
        if not self:
            return 0
        depth_max__left = self.left.maxDepth() if self.left else 0
        depth_max__right = self.right.maxDepth() if self.right else 0
        candidates = [depth_max__left + depth_max__right]
        if self.left:
            candidates.append(self.left.diameter())
        if self.right:
            candidates.append(self.right.diameter())
        return max(candidates)

    def diameter(self) -> int:
        """Recursive relation:
            diameter = max{depth_max(left) + depth_max(right), diameter(left), diameter(right)}.
        Time complexity: O(n), space complexity: Ω(log(n)) ∩ O(n), where `n` is the number of nodes.
        Space complexity is due to recursion from the depth of tree.
        We cache the results of maxDepth to reduce time complexity.
        """
        if not self:
            return 0
        cache_depth_max: dict[int, int] = {}

        def _diameter_inner(root: BinaryTreeNode) -> int:
            nonlocal cache_depth_max
            depth_max__left = depth_max__right = 0
            diameter__left = diameter__right = 0
            if root.left:
                if id(root.left) not in cache_depth_max:
                    cache_depth_max[id(root.left)] = root.left.maxDepth()
                depth_max__left = cache_depth_max[id(root.left)]
                diameter__left = _diameter_inner(root=root.left)
            if root.right:
                if id(root.right) not in cache_depth_max:
                    cache_depth_max[id(root.right)] = root.right.maxDepth()
                depth_max__right = cache_depth_max[id(root.right)]
                diameter__right = _diameter_inner(root=root.right)
            return max(
                [depth_max__left + depth_max__right, diameter__left, diameter__right]
            )

        return _diameter_inner(root=self)

    def diameter_1pass(self) -> int:
        """Recursive relation:
            diameter = max{depth_max(left) + depth_max(right), diameter(left), diameter(right)}.
        We use DFS for both maximum depth and diameter simultaneously.
        Time complexity: O(n), space complexity: O(1), where `n` is the number of nodes.
        """
        diameter__max = 0

        def _maxDepth_dfs(root: BinaryTreeNode | None = self) -> int:
            nonlocal diameter__max
            if not root:
                return 0
            depth_max__left = _maxDepth_dfs(root=root.left)
            depth_max__right = _maxDepth_dfs(root=root.right)
            diameter_cur = depth_max__left + depth_max__right
            diameter__max = max(diameter_cur, diameter__max)
            return 1 + max(depth_max__left, depth_max__right)

        _maxDepth_dfs()
        return diameter__max

    def searchBST(self, val: int) -> BinaryTreeNode | None:
        if self.data == val:
            return self
        elif val < self.data and self.left:
            return self.left.searchBST(val)
        elif val > self.data and self.right:
            return self.right.searchBST(val)
        return None
