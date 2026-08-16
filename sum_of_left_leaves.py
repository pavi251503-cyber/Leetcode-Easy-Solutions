"""
Problem name: Sum of left leaves
Problem no: 404
Difficulty: Easy
"""
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        total = 0
        
        # Check if left child exists
        if root.left:
            # Check if left child is a leaf
            if root.left.left is None and root.left.right is None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
        
        # Check right subtree
        total += self.sumOfLeftLeaves(root.right)
        
        return total