# Created by muzhi1991 at 2024/12/25 10:27
# leetgo: 1.4.11
# https://leetcode.cn/problems/sort-list/

from typing import *
from leetgo_py import *
import random

random.seed(42)
# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortChunk(self, head, chunk_size):
        res = None  # 开头 node
        pre = None  # fix: 前一个 chunk 的最后一个 node，续起来
        p = head
        while p is not None:
            t1 = 0
            t2 = 0
            p1 = p
            p2 = p  # 下一个chunk指针
            # print("bef", p.val, p1.val)
            #
            # 这里容易犯的错误就是p1 提前终止了，不是取中点。。是每个chunk 要尽量渠道 size 的大
            while p1 and t1 < chunk_size:
                p1 = p1.next
                t1 += 1
                if p2:
                    p2 = p2.next
                    t2 += 1
                    if p2 is not None:
                        p2 = p2.next
                        t2 += 1

            # print(p.val, p1.val)
            # print(t1, t2, t2 - t1)
            t2 = t2 - t1  # 第二个减去第一个，才是第二个 chunk 的长度
            n = None  # 归并的指针
            # 归并
            # p和 p1 分别是第一个 chunk 和第二个 chunk 的 head，对他们进行归并
            # 注意点：
            # 1. 注意两个 chunk 不一样长的情况，注意判断，这里用的计数器判断的，更好的是吧这两个链表构造一下 tail None，然后归并起来方便
            # 2. 归并完了，需要做两个事情，请示后一个 chunk 的结尾设置 None，否则有概率死循环。第二个是保留最后一个 chunk 的 tail 的指针，方便下一轮找到新 head 的时候连上去
            while (t1 > 0 and p) or (t2 > 0 and p1):
                # print("a", n.val if n else None, "p", p.val if p else None, "p1", p1.val if p1 else None, t1, t2)
                if t1 == 0:
                    next = p1
                    p1 = p1.next
                    t2 -= 1
                elif t2 == 0:
                    next = p
                    p = p.next
                    t1 -= 1
                else:
                    if p.val < p1.val:
                        next = p
                        p = p.next
                        t1 -= 1
                    else:
                        next = p1
                        p1 = p1.next
                        t2 -= 1
                # print("next", next.val)
                if n is None:
                    n = next
                    if pre:
                        pre.next = n
                    if res is None:
                        res = n
                else:
                    # print("n next", n.val, next.val)
                    n.next = next
                    n = n.next

            n.next = None  # fix:注意置为空，否则有些结尾不是空会死循环

            # p=xx
            pre = n  # 保留最后的 tail 节点，方便下一轮连上
            p = p2
        return res

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chunk_size = 1
        cnt = 0
        p = head
        while p:
            p = p.next
            cnt += 1

        res = head
        while chunk_size < cnt:
            # print("chunk size", chunk_size)
            res = self.sortChunk(res, chunk_size)
            # p = res
            # while p:
            #     print(p.val)
            #     p = p.next
            chunk_size *= 2
        # p = res
        # while p:
        #     print(p.val)
        #     p = p.next
        # res = self.sortChunk(res, chunk_size * 2)
        # p = res
        # while p:
        #     print(p.val)
        #     p = p.next
        return res

    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head
    #
    #     pre, p, c = None, head, head
    #     while c is not None and c.next is not None:
    #         pre = p
    #         p = p.next
    #         c = c.next
    #         while c and random.random() < 0.5:
    #             # print(c)
    #             c = c.next
    #     if pre is not None:
    #         pre.next = p.next
    #     if p != head:
    #         cur = head
    #     else:
    #         cur = p.next
    #     p.next = None
    #     left, left_cur = None, None
    #     right, right_cur = None, None
    #     equal, equal_cur = None, None
    #     while cur is not None:
    #         if cur.val == p.val:
    #             if equal is None:
    #                 equal = cur
    #             else:
    #                 equal_cur.next = cur
    #             equal_cur = cur
    #         elif cur.val < p.val:
    #             if left is None:
    #                 left = cur
    #             else:
    #                 left_cur.next = cur
    #             left_cur = cur
    #         else:
    #             if right is None:
    #                 right = cur
    #             else:
    #                 right_cur.next = cur
    #             right_cur = cur
    #         next = cur.next
    #         cur.next = None
    #         cur = next
    #     # print(left, right, equal)
    #     ll = self.sortList(left)
    #     rr = self.sortList(right)
    #
    #     if equal is not None:
    #         p.next = equal
    #     cur = p
    #     while cur.next is not None:
    #         cur = cur.next
    #     cur.next = rr
    #
    #     if ll is None:
    #         return p
    #
    #     cur = ll
    #     while cur.next is not None:
    #         cur = cur.next
    #     cur.next = p
    #     return ll


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    # ll = [4, 2, 1, 3]
    # ll = [-1, 5, 3, 4, 0]
    # ll = [55, 43, 12, 1]
    # head = None
    # pre = None
    # for l in ll:
    #     node = ListNode(l)
    #     if pre is None:
    #         pre = node
    #         head = node
    #     else:
    #         pre.next = node
    #     pre = node
    ans = Solution().sortList(head)
    print("\noutput:", serialize(ans, "ListNode"))
