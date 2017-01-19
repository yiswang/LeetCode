#!/usr/bin/python

###############################################################################
#
# LeetCode 24. Swap Nodes in Pairs
#
# Difficulty: Easy
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.
# 
###############################################################################

import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printLink(head):
    if not head:
        print head, "\n"
        return

    node = head
    while node != None:
        print "%d" % node.val,
        node = node.next
    print ""

def constructLink(num_list):
    if num_list == None or num_list == []:
        return None

    head = ListNode(num_list[0])
    pre_node = head
    for i in xrange(1, len(num_list)):
        node = ListNode(num_list[i])
        pre_node.next = node
        pre_node = node
    return head



class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre_node, pre_node.next = self, head
        while pre_node.next and pre_node.next.next:
            a = pre_node.next
            b = a.next
            a.next, b.next, pre_node.next = b.next, a, b
            pre_node = a
        return self.next


if __name__ == "__main__":
#     pdb.set_trace()

    test_cases = [
        [],
        [1],
        [1,2],
        [1,2,3],
        [1,2,3,4],
        [1,2,3,4,5],
        [1,2,3,4,5,6]
    ]

    solu = Solution()
    for num_list in test_cases:
        print num_list
        head = constructLink(num_list)
        printLink(head)
        new_head = solu.swapPairs(head)
        printLink(new_head)
        print "\n"
