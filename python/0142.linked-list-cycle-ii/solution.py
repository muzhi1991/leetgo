# Created by muzhi1991 at 2024/12/30 09:45
# leetgo: 1.4.11
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def f(self, head, p):
        p1 = head
        p2 = head
        cnt1 = 0
        cnt2 = 0
        t = 0
        while True:
            p1 = p1.next
            cnt1 += 1
            p2 = p2.next
            cnt2 += 1
            if p and p2 == p:
                t += 1
            if p2 == p1 and cnt1 != 1:
                break
            if p2 is not None:
                p2 = p2.next
                cnt2 += 1
                if p and p2 == p:
                    t += 1
                if p2 == p1:
                    break
            else:
                return None, None, None, None
        return (p1, t, cnt2, cnt1)

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r, _, cnt2, cnt1 = self.f(head, None)
        if not r:
            return None

        diff = cnt2 - cnt1

        p = head
        while diff > 0:
            p = p.next
            diff -= 1
        r, _, cnt2, cnt1 = self.f(p, None)
        cc = cnt2 - cnt1
        print(cnt2, cnt1, cc)
        while cc > 0:
            p = p.next
            cc -= 1
        print(p.val)
        return p


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    # pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head)
    print("\noutput:", serialize(ans, "ListNode"))
