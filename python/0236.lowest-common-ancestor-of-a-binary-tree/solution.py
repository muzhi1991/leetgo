# Created by muzhi1991 at 2024/12/13 01:26
# leetgo: 1.4.11
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
 思考过程：
* tree 问题-> 递归
* 定义子问题：左子树和右子树**同时**都满足 “包含 q **或者** q”

定义函数功能(返回值的复用）：
1. p q都能找到 返回最近公共祖先 
2. p q 找到一个，返回p/q 
3. 都没找到 返回null

"""


class Solution:
    # def func(self, root: "TreeNode", p: "TreeNode", q: "TreeNode", buf: Set):
    #     # print(buf)
    #     if root is None:
    #         return
    #     bufl, bufr = set(), set()
    #     res1 = self.func(root.left, p, q, bufl)
    #     # print(bufl)
    #     if res1:
    #         return res1
    #     res2 = self.func(root.right, p, q, bufr)
    #     # print(bufr)
    #     if res2:
    #         return res2
    #     if (p.val in bufl or p.val == root.val) and (q.val in bufr or q.val == root.val):
    #         return root
    #     if (p.val in bufr or p.val == root.val) and (q.val in bufl or q.val == root.val):
    #         return root
    #     buf.add(root.val)
    #     buf.update(bufl)
    #     buf.update(bufr)
    #     # print(root.val, "-->", bufl, bufr, buf)
    #     return None

    # def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    #     print("start")
    #     buf = set()
    #     return self.func(root, p, q, buf)

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if root is None:
            return None
        if root == p or root == q:
            return root
        a1 = self.lowestCommonAncestor(root.left, p, q)
        a2 = self.lowestCommonAncestor(root.right, p, q)
        if a1 and a2:
            return root
        return a1 if a1 else a2


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)
    print("\noutput:", serialize(ans, "TreeNode"))
