# Created by muzhi1991 at 2024/12/20 11:06
# leetgo: 1.4.11
# https://leetcode.cn/problems/reverse-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre = None
        cur = head
        while cur.next is not None:
            cur.next, pre, cur = pre, cur, cur.next
        cur.next = pre
        return cur


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().reverseList(head)
    print("\noutput:", serialize(ans, "ListNode"))
