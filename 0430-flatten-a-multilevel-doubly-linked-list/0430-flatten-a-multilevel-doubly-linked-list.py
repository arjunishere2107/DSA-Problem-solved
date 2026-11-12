"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        if head is None:
            return None

        self.flattenDFS(head)
        return head

    def flattenDFS(self, curr):

        last = curr

        while curr:

            nextNode = curr.next

            if curr.child:

                childHead = curr.child

                childTail = self.flattenDFS(childHead)

                curr.next = childHead
                childHead.prev = curr

                curr.child = None

                if nextNode:
                    childTail.next = nextNode
                    nextNode.prev = childTail

                last = childTail

            else:
                last = curr

            curr = nextNode

        return last
        