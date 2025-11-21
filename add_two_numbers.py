# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each node contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the numbers do not contain any leading zeros, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Starting point for the resulting linked list
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            value = total % 10

            current.next = ListNode(value)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

