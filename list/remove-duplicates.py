class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        pNode = head
        while pNode:
            while pNode.next and pNode.next.val == pNode.val:
                pNode.next = pNode.next.next
        return head