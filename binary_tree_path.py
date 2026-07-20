"""
Problem name:Binary Tree Path
Probelm no: 257
Difficulty: Easy
"""

class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            # If it's a leaf node
            if not node.left and not node.right:
                result.append(path)
                return

            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return result