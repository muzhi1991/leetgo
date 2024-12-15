# Created by muzhi1991 at 2024/12/14 01:25
# leetgo: 1.4.11
# https://leetcode.cn/problems/palindrome-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
 回文不能用括号匹配的栈 [1,1,2,2]
 最简单计算转成 list，双指针遍历
 还有个思路是：全部放入 stack，然后 pop，结果和从头遍历对比是否相关
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        p = head
        while p is not None:
            stack.append(p.val)
            p = p.next
        p = head
        while len(stack) > 0:
            v = stack.pop()
            if v != p.val:
                return False
            p = p.next
        return True


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().isPalindrome(head)
    print("\noutput:", serialize(ans, "boolean"))
