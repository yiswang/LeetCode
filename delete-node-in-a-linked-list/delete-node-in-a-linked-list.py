#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        delete-node-in-a-linked-list.py
# Create Date: 2017-02-24
# Usage:       delete-node-in-a-linked-list.py
# Description:
#
# LeetCode problem 237. Delete Node in a Linked List Add to List
#
# Difficulty: Easy
#
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
# 
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
# with value 3, the linked list should become 1 -> 2 -> 4 after calling your
# function.
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
# It can only replace the value of that node with the value of the next node,
# but can not really delete that node.
#
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        
if __name__ == "__main__":
    test_cases = [
        ([1,2], 1),
        ([1,2,3], 2),
    ]
    solu = Solution()
    for num_list, idx in test_cases:
        node = head = constructLink(num_list)
        for _ in xrange(idx - 1):
            node = node.next
        printLink(head)
        solu.deleteNode(node)
        printLink(head)
        print "\n"    
