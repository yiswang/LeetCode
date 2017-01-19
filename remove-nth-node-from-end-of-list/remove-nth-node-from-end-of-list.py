#!/usr/bin/python

###############################################################################
#
# LeetCode 19. Remove Nth Node From End of List
#
# Difficulty: Easy
#
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes
#    1->2->3->5.
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

def printLink(head):
    node = head
    while node != None:
        print "%d" % node.val,
        node = node.next

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None or n==0:
            return head

        dummy = node1 = ListNode(0)
        node2 = ListNode(0)
        node1.next = node2.next = head
        for _ in xrange(n):
            node2 = node2.next
        while node2.next:
            node1 = node1.next
            node2 = node2.next
        node1.next = node1.next.next
        return dummy.next

        
if __name__ == "__main__":
#     pdb.set_trace()

    test_cases = [
        ([], 0),
        ([1], 1),
        ([1], 0),
        ([1,2,3,4,5], 1),
        ([1,2,3,4,5], 2),
        ([1,2,3,4,5], 5),
    ]
    solu = Solution()
    for num_list, n in test_cases:
        head = constructLink(num_list)
        head = solu.removeNthFromEnd(head, n)
        printLink(head)
        print "\n"
