#!/usr/bin/python

###############################################################################
#
# LeetCode 19. Remove Nth Node From End of List
#
# Total Accepted: 151878
# Total Submissions: 473578
# Difficulty: Easy
# Contributors: Admin
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
#
# Given n will always be valid.
#
# Try to do this in one pass.
# 
###############################################################################

import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node_list = [head]
        count = 1
        node = head.next
        while node != None:
            count += 1
            node_list += [node]
            node = node.next

        if n == count:
            node = head.next
            head.next = None
            return node

        index = count - n
        node_list[index-1].next = node_list[index].next
        node_list[index].next = None
        
        return head

        
def printList(head):
    node = head
    while node != None:
        print "%d" % node.val,
        node = node.next


if __name__ == "__main__":
    pdb.set_trace()

    num_list = [1]
    num_list = [1, 2, 3, 4, 5]
    head = ListNode(num_list[0])
    pre_node = head
    for i in xrange(1, len(num_list)):
        node = ListNode(num_list[i])
        pre_node.next = node
        pre_node = node

    solu = Solution()
    head = solu.removeNthFromEnd(head, 5)
    printList(head)
