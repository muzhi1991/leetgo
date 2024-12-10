# Created by muzhi1991 at 2024/12/11 01:22
# leetgo: 1.4.11
# https://leetcode.cn/problems/intersection-of-two-linked-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    intersectVal: int = deserialize("int", read_line())
    listA: ListNode = deserialize("ListNode", read_line())
    listB: ListNode = deserialize("ListNode", read_line())
    skipA: int = deserialize("int", read_line())
    skipB: int = deserialize("int", read_line())
    ans = Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB)
    print("\noutput:", serialize(ans, "ListNode"))
