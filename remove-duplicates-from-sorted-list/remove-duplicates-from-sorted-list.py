#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        remove-duplicates-from-sorted-list.py
# Create Date: 2017-01-29
# Usage:       remove-duplicates-from-sorted-list.py
# Description:
#
# LeetCode problem 83. Remove Duplicates from Sorted List
#
# Difficulty: Easy
# 
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3. 
#
###############################################################################


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printLink(head):
    if head == None:
        print "None"
        return

    node = head
    while node.next != None:
        print "%d ->" % node.val,
        node = node.next
    print "%d" % node.val

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


# Run time on LeetCode: 56ms. Beats 78%
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

        
if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [1,2],
        [1,2,3],
        [1,2,2],
        [1,1,2],
        [1,1,2,2],
        [1,1,2,3],
        [1,1,2,3,3],
        [1,1,2,3,4,4],
        [1,1,1,2,3,3,3,4,5,5],
        [1,1,1,2,3,3,3,4,5,5,5],
    ]
    solu = Solution()
    for num_list in test_cases:
        head = constructLink(num_list)
        print "Before removal:"
        printLink(head)
        head = solu.deleteDuplicates(head)
        print "After removal:"
        printLink(head)
        print "\n"
