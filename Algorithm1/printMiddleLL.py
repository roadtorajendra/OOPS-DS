'''Hint:Think of two pointers technique with slow runner and fast runner.
Both slow runner and fast runner are initialized to head node.
Each iteration, fast runner moves two steps forward while the slow one moves one steps only.
When fast runner meets the empty node (i.e., NULL) on the tail, the slow one will be right on the node of midpoint.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head): 
        slow, fast = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break
            slow = slow.next
        return slow