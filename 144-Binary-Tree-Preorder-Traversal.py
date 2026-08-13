# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def pot(self,root):
        if root==None:
            return
        self.ans.append(root.val)
        self.pot(root.left)
        self.pot(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.pot(root)
        return self.ans
        
        