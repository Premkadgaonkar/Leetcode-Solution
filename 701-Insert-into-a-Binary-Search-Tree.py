# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=TreeNode(val)
        if root==None:
            return temp
        
        curr=root
        while curr!=None:
            if curr.val>val:
                if curr.left!=None:
                    curr=curr.left
                else:
                    curr.left=temp
                    break
            else:
                if curr.right!=None:
                    curr=curr.right
                else:
                    curr.right=temp
                    break
        return root
        