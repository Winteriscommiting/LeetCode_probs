# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rs=[]
        def inord(node):
            if not node:
                return []
            inord(node.left)
            rs.append(node.val)
            inord(node.right)
        inord(root)
        return rs