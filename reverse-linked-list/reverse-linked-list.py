#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        reverse-linked-list.py
# Create Date: 2017-02-21
# Usage:       reverse-linked-list.py
# Description:
#
# LeetCode problem 206. Reverse Linked List Add to List
#
# Difficulty: Easy
#
# Reverse a singly linked list.
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
        

#
# Run time on LeetCode: 48ms, beat 87.25%
#
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        preNode = None
        curNode = head
        while curNode:
            nextNode = curNode.next
            curNode.next = preNode  
            preNode = curNode
            curNode = nextNode
        return preNode


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4],
    ]
    solu = Solution()
    for array in test_cases:
        head = constructLink(array)
        printLink(head)
        res = solu.reverseList(head)
        printLink(res)
        print ""
