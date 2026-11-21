# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode=[root]
        d={}
        while mode:
            a=mode.pop()
            if a.val not in d:
                d[a.val]=1
            else:
                d[a.val]+=1
            if a.left:
                mode.append(a.left)
            if a.right:
                mode.append(a.right)
        m=max(d.values())
        res=[]
        for i,j in d.items():
            if j==m:
                res.append(i)
        return res