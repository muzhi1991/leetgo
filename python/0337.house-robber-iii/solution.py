# Created by muzhi1991 at 2025/01/07 10:32
# leetgo: 1.4.11
# https://leetcode.cn/problems/house-robber-iii/

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
    def f(self, root: Optional[TreeNode], buf) -> int:
        if root and not root.left and not root.right:
            print(root.val)
        if not root:
            return 0
        if root in buf:
            return buf[root]

        res = root.val
        # option 1: choosen
        if root.left:
            res += self.f(root.left.left, buf) + self.f(root.left.right, buf)
        if root.right:
            res += self.f(root.right.left, buf) + self.f(root.right.right, buf)
        # option not chosen
        res2 = self.f(root.left, buf) + self.f(root.right, buf)
        rr = max(res, res2)
        buf[root] = rr
        return rr

    def rob(self, root: Optional[TreeNode]) -> int:
        buf = {}
        return self.f(root, buf)


# @lc code=end

if __name__ == "__main__":
    line = "[79,99,77,null,null,null,69,null,60,53,null,73,11,null,null,null,62,27,62,null,null,98,50,null,null,90,48,82,null,null,null,55,64,null,null,73,56,6,47,null,93,null,null,75,44,30,82,null,null,null,null,null,null,57,36,89,42,null,null,76,10,null,null,null,null,null,32,4,18,null,null,1,7,null,null,42,64,null,null,39,76,null,null,6,null,66,8,96,91,38,38,null,null,null,null,74,42,null,null,null,10,40,5,null,null,null,null,28,8,24,47,null,null,null,17,36,50,19,63,33,89,null,null,null,null,null,null,null,null,94,72,null,null,79,25,null,null,51,null,70,84,43,null,64,35,null,null,null,null,40,78,null,null,35,42,98,96,null,null,82,26,null,null,null,null,48,91,null,null,35,93,86,42,null,null,null,null,0,61,null,null,67,null,53,48,null,null,82,30,null,97,null,null,null,1,null,null]"
    root: TreeNode = deserialize("TreeNode", line)
    # root: TreeNode = deserialize("TreeNode", read_line())
    # root: TreeNode = deserialize("TreeNode", "[3,2,3,null,3,null,1]")
    # root: TreeNode = deserialize("TreeNode", "[2,1,3,null,4]")
    # root: TreeNode = deserialize("TreeNode", "[5,3,6,1,4,null,null,null,2]")
    ans = Solution().rob(root)
    print("\noutput:", serialize(ans, "integer"))
