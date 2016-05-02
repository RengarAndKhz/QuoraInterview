# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heapify, heapreplace, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = pointer = ListNode(0)
        heap = [(node.val, node) for node in lists if node]
        heapify(heap)
        while heap:
            value, n = heap[0]
            if n.next is None:
                heappop(heap)
            else:
                heapreplace(heap, (n.next.val, n.next))
            pointer.next = n
            pointer = pointer.next
        return result.next