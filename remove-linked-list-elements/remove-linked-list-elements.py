#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        remove-linked-list-elements.py
# Create Date: 2017-02-20
# Usage:       remove-linked-list-elements.py
# Description:
#
# LeetCode problem 203. Remove Linked List Elements Add to List
#
# Difficulty: Easy
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
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


# Run time on LeetCode: 159ms, beats 9.83%
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy, dummy.next = self, head 
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next


        
if __name__ == "__main__":
    test_cases = [
        ([], 0),
        ([1], 0),
        ([1], 1),
        ([1,2], 1),
        ([1,2], 2),
        ([1,2,3], 2),
    ]
    solu = Solution()
    for num_list, val in test_cases:
        head = constructLink(num_list)
        print "val: %d" % val
        print "Before removal:"
        printLink(head)
        head = solu.removeElements(head, val)
        print "After removal:"
        printLink(head)
        print "\n"
