#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Medium (28.13%)
# Likes:    2586
# Dislikes: 1592
# Total Accepted:    319.4K
# Total Submissions: 1.1M
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
  '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val
# is the value of the current node, and next is a pointer/reference to the next
# node.
# If you want to use the doubly linked list, you will need one more attribute
# prev to indicate the previous node in the linked list. Assume all nodes in
# the linked list are 0-indexed.
# 
# Implement the MyLinkedList class:
# 
# 
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the index^th node in the linked list. If
# the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of
# the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the
# linked list.
# void addAtIndex(int index, int val) Add a node of value val before the
# index^th node in the linked list. If index equals the length of the linked
# list, the node will be appended to the end of the linked list. If index is
# greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the index^th node in the linked list, if
# the index is valid.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# 
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
# 
# 
#

# @lc code=start
class MyLinkedList:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        cur = self
        for _ in range(index):
            if not cur.next: break
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self = MyLinkedList(val, self)

    def addAtTail(self, val: int) -> None:
        cur = self
        while cur.next:
            cur = cur.next
        cur.next = MyLinkedList(val)

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = MyLinkedList(0, self)
        cur = dummy
        for _ in range(index):
            if not cur.next: break
            cur = cur.next
        cur.next = MyLinkedList(val, cur.next)
        self = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = MyLinkedList(0, self)
        cur = dummy
        for _ in range(index):
            if not cur.next.next: return
            cur = cur.next
        cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

