# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=True
    def height(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        lefttree=self.height(root.left)
        righttree=self.height(root.right)

        if abs(lefttree-righttree)>1:
            self.ans=False

        return max(lefttree,righttree)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
        