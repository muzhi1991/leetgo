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

"""
思路一：如果两个链相同长度，我们就可用两个指针都从头开始遍历，遇到相等的就是相交点，到 none 了就是不相交，因此可以先计算两者 diff 长度，长的那个先走 diff 步，此时就相等了
思路二：假设一个长度 A+C，另外一个是 B+C，（AB 是不相交部分的长度，C 是共同长度）核心就是 遍历完一个立刻 从头遍历第二个，利用他们都是 A+B+C， 也就是说他们必然同时到达另外一个的终点，如果有相等节点就必然会相遇，否则最后都是 none
"""

# class Solution:
#    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#        # print("here")
#        pointA = headA
#        pointB = headB
#        if pointA == pointB:
#            return pointA
#        if not pointA or not pointB:
#            return None
#
#        while pointA.next is not None and pointB.next is not None:
#            pointA = pointA.next
#            pointB = pointB.next
#            if pointA == pointB:
#                return pointA
#
#        head = pointA.next if pointB.next is None else pointB.next
#        if head is None:
#            return None
#        n = 1
#        while head.next is not None:
#            head = head.next
#            n += 1
#
#        start = headA if pointA.next is not None else headB
#        pointB = headB if pointA.next is not None else headA
#
#        pointA = start
#        for i in range(n):
#            pointA = pointA.next
#        if pointA == pointB:
#            return pointA
#
#        while pointA.next is not None and pointB.next != None:
#            pointA = pointA.next
#
#            pointB = pointB.next
#            if pointA == pointB:
#                return pointA
#
#        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        if pa == pb:
            return pa
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    # intersectVal: int = deserialize("int", read_line())
    la: ListNode = deserialize("list", read_line())
    lb: ListNode = deserialize("list", read_line())
    listA = []
    listB = []

    # skipA: int = deserialize("int", read_line())
    # skipB: int = deserialize("int", read_line())
    ans = Solution().getIntersectionNode(listA, listB)
    print("\noutput:", serialize(ans, "ListNode"))
