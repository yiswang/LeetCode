#!/usr/bin/python

###############################################################################
#
# LeetCode 21. Merge Two Sorted Lists
#
# Difficulty: Easy
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
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

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if None in [l1, l2]:
            return l1 or l2
        
        dummy = pre_node = ListNode(0)
        dummy.next = l1
        while l2 != None:
            while l1 != None and l1.val <= l2.val:
                pre_node = l1
                l1 = l1.next
            pre_node.next = l2
            pre_node = l2
            l2 = l1
            l1 = pre_node.next

        return dummy.next


if __name__ == "__main__":
#     pdb.set_trace()

#     num_list1 = [4, 5, 6, 7, 10, 11, 12]
    num_list1 = [1,2,8]
    head1 = constructLink(num_list1)

    num_list2 = [5,7, 7, 7, 9]
    head2 = constructLink(num_list2)

    solu = Solution()
    head = solu.mergeTwoLists(head1, head2)
    printLink(head)
