#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (37.61%)
# Likes:    9429
# Dislikes: 1434
# Total Accepted:    926.1K
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, l = head, 0
        while cur:
            cur = cur.next
            l += 1
        # corner case：如果链表长度为 0
        if not l:
            return head
        k %= l
        # corner case：如果实际不作旋转
        if not k:
            return head
        cur = head
        for _i in range(l - k - 1):
            cur = cur.next
        next = cur.next
        cur.next = None
        cur = next
        while cur and cur.next:
            cur = cur.next
        cur.next = head
        return next


# @lc code=end
