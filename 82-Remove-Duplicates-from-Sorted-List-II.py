# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(-1)
        temp.next=head
        prev=temp
        cur=head
        
        while cur!=None and cur.next!=None:
            if cur.val==cur.next.val:
                while cur.next!=None and cur.val==cur.next.val:
                    cur=cur.next
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next

        return temp.next
        