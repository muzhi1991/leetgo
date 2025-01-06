# Created by muzhi1991 at 2024/12/31 10:36
# leetgo: 1.4.11
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/

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
    def sortTree(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            root.dp = root.val
            return
        if root.right is None:
            self.sortTree(root.left)
            mm = max(root.left.dp + root.val, root.val)
        elif root.left is None:
            self.sortTree(root.right)
            mm = max(root.right.dp + root.val, root.val)
        else:
            self.sortTree(root.left)
            self.sortTree(root.right)
            mm = max(root.left.dp + root.val, root.right.dp + root.val, root.val)
        root.dp = mm

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sortTree(root)
        res = -1e9
        stack = [root]
        while stack:
            n = stack.pop()
            dp=n.dp
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
            if n.left and n.right:
                dp = max(dp, n.left.dp + n.val + n.right.dp)
            if dp > res:
                res = dp
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxPathSum(root)
    print("\noutput:", serialize(ans, "integer"))
