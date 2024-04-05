#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (56.14%)
# Likes:    7232
# Dislikes: 847
# Total Accepted:    608.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1, head2 = ListNode(0), ListNode(0)
        cur1, cur2 = head1, head2
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        # 易错点：避免成环——后半部分链表的尾端，箭头需要置空
        cur2.next = None
        cur1.next = head2.next
        return head1.next
# @lc code=end
