# Created by muzhi1991 at 2024/12/30 11:16
# leetgo: 1.4.11
# https://leetcode.cn/problems/linked-list-cycle/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p1 = head
        p2 = head
        while True:
            p1 = p1.next
            p2 = p2.next
            if p2 is not None:
                p2 = p2.next
                if p2 is None:
                    return False
            else:
                return False
            if p1 is p2:
                break
        return True


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().hasCycle(head, pos)
    print("\noutput:", serialize(ans, "boolean"))
