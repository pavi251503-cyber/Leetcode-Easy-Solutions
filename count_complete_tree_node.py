'''Problem name: Count Complete Tree Nodes
Difficulty: Easy
Problem No: 222
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = 0
        right_height = 0

        left = root
        right = root

        while left:
            left_height += 1
            left = left.left

        while right:
            right_height += 1
            right = right.right

        if left_height == right_height:
            return (2 ** left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)

sol = Solution()
print(sol.countNodes(root))