#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (74.16%)
# Likes:    18737
# Dislikes: 345
# Total Accepted:    3.2M
# Total Submissions: 4.4M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化前后两个指针
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        # 因为循环结束的时候curr已经是空指针，因此返回的是prev
        return prev.next

    # 递归解法：后序遍历
    def reverseListDFS1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 因为是后序遍历，我们假定前面的都处理好了，后面的还没处理好
        def dfs(curr, prev):
            # 最后返回尾节点
            if not curr: return prev
            next = curr.next
            # 每次递归只改变一个箭头
            curr.next = prev
            return dfs(next, curr)
        return dfs(head, None)

    # 递归解法：后序遍历
    def reverseListDFS2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(curr):
            # 边界条件
            if not curr or not curr.next: return curr
            # 后序遍历
            ret = dfs(curr.next)
            # 主逻辑
            curr.next.next = curr
            # 现在先置空并没有关系，因为 dfs 过程结束后会自动回推一格
            curr.next = None
            return ret
        return dfs(head)

# @lc code=end

