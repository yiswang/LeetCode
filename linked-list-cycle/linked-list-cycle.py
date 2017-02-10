#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        linked-list-cycle.py
# Create Date: 2017-02-08
# Usage:       linked-list-cycle.py
# Description:
#
# LeetCode problem 141. Linked List Cycle
#
# Difficulty: Easy
#
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?
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

def constructCycleLink(num_list):
    if num_list == None or num_list == []:
        return None

    head = ListNode(num_list[0])
    pre_node = head
    for i in xrange(1, len(num_list)):
        node = ListNode(num_list[i])
        pre_node.next = node
        pre_node = node
    pre_node.next = head
    return head


# Run time on LeetCode: 78ms. Beats 82.53%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = b = head
        while a and a.next and b:
            a = a.next.next
            b = b.next
            if a == b:
                return True
        return False

        
if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [1,2],
        [1,2,3],
    ]
    solu = Solution()
    for num_list in test_cases:
        head = constructLink(num_list)
        printLink(head)
        res = solu.hasCycle(head)
        print res

        head = constructCycleLink(num_list)
        res = solu.hasCycle(head)
        print res

        print "\n"
