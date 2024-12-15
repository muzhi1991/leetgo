# Created by muzhi1991 at 2024/12/15 10:52
# leetgo: 1.4.11
# https://leetcode.cn/problems/invert-binary-tree/

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        a = self.invertTree(root.left)
        b = self.invertTree(root.right)
        root.left = b
        root.right = a
        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().invertTree(root)
    print("\noutput:", serialize(ans, "TreeNode"))
