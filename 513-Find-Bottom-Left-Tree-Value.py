# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1
    def enqueue(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def dequeue(self):
        if len(self.q)==0:
            return -1
        x=self.q[self.front]
        self.front+=1
        if self.front==len(self.q):
            self.front=-1
            self.q=[]
        return x
    def size(self):
        if self.front==-1:
            return 0
        return len(self.q)-self.front     

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans=[]
        if root is None:
            return ans
        q=Queue()
        q.enqueue(root)
        ans.append((root.val))

        while q.size()>0:
            l=q.size()
            level=[]
            for i in range(l):
                front=q.dequeue()
                if front.left!=None:
                    q.enqueue(front.left)
                    level.append(front.left.val)
                if front.right!=None:
                    q.enqueue(front.right)
                    level.append(front.right.val)

            if len(level)!=0:
                ans.append(level[0])
        
        return ans[-1]