# Created by muzhi1991 at 2025/01/02 14:08
# leetgo: 1.4.11
# https://leetcode.cn/problems/path-sum-iii/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        res = 0
        stack = [root]
        mm = {}
        mm[0] = 1  # fix: 前缀为 0要默认加到里面！！
        ss = 0
        visited = set()
        while stack:
            n = stack.pop()
            if n in visited:
                mm[ss] -= 1
                ss -= n.val
                # print(n.val)
            else:
                visited.add(n)
                stack.append(n)
                ss += n.val
                # fix: 注意位置！！，ss 先计算选前缀再放入前缀，否则再 targetSum 为 0 的时候会把自己重新选上
                if (ss - targetSum) in mm:
                    # print("hit", n.val)
                    res += mm[ss - targetSum]

                if ss not in mm:
                    mm[ss] = 1
                else:
                    mm[ss] += 1
                # print(n.val, ss, ss - targetSum, mm)
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)
        return res


# def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#     if not root:
#         return 0
#     res = 0
#     stack = [root]
#     i = 0
#     while i < len(stack):
#         cur = stack[i]
#         if cur.left:
#             stack.append((cur.left))
#         if cur.right:
#             stack.append(cur.right)
#         i += 1
#     for n in reversed(stack):
#         n.ss = [n.val]
#         # print(n.val,n.left,n.right)
#         if not n.left and not n.right:
#             pass
#         else:
#             if n.left:
#                 for v in n.left.ss:
#                     n.ss.append(v + n.val)
#             if n.right:
#                 for v in n.right.ss:
#                     n.ss.append(v + n.val)
#         for v in n.ss:
#             if v == targetSum:
#                 res += 1
#         # print(n.val, n.ss)
#     return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().pathSum(root, targetSum)
    print("\noutput:", serialize(ans, "integer"))
