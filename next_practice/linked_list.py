# 链表成对调换
"""

1->2->3->4转换成2->1->4->3.


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    print(l1.val,
          l1.next.val,
          l1.next.next.val,
          l1.next.next.next.val)

    solution = Solution()
    solution.swapPairs(l1)
    
    # print((l1.val, l1.next.val), (l2.val, l2.next.val), (l3.val, l3.next.val), (l4.val, l4.next.val), sep='\n')
    print(l2.val,
          l2.next.val,
          l2.next.next.val,
          l2.next.next.next.val)
