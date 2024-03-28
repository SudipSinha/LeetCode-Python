"""Definition for a binary tree node."""
#   TODO
#   Deepcopy

from __future__ import annotations

from collections import deque


class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, BinaryTreeNode)
            and self.val == other.val
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
            if index >= len(nums) or nums[index] is None:
                return None
            node = BinaryTreeNode(val=nums[index])
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
        return result_left + [self.val] + result_right

    def preorderTraversal_recur(self) -> list[int]:
        if not self:
            return []
        result_left = self.left.preorderTraversal_recur() if self.left else []
        result_right = self.right.preorderTraversal_recur() if self.right else []
        return [self.val] + result_left + result_right

    def postorderTraversal_recur(self) -> list[int]:
        if not self:
            return []
        result_left = self.left.postorderTraversal_recur() if self.left else []
        result_right = self.right.postorderTraversal_recur() if self.right else []
        return result_left + result_right + [self.val]

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
            rsv.append(queue[0].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return rsv
