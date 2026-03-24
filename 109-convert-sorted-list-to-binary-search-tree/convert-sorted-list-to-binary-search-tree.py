# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        def findMiddle(ListNode):
            prev=None
            slow=head
            fast=head
            while(fast and fast.next):
                prev=slow
                fast=fast.next.next
                slow=slow.next

            
            if prev:
                prev.next=None
            
            return slow
        
        if head.next is None:
            return TreeNode(head.val)

        mid=findMiddle(head)

        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)

        return root