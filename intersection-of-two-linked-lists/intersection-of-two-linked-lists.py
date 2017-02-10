#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        intersection-of-two-linked-lists.py
# Create Date: 2017-02-09
# Usage:       intersection-of-two-linked-lists.py
# Description:
#
# LeetCode problem 160. Intersection of Two Linked Lists
#
# Difficulty: Easy
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# 
# For example, the following two linked lists:
# 
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.
# 
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.  The linked
# lists must retain their original structure after the function returns.  You
# may assume there are no cycles anywhere in the entire linked structure.  Your
# code should preferably run in O(n) time and use only O(1) memory.
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

def constructLinkWithUniqVals(num_list, node_list):
    if num_list == None or num_list == []:
        return None

    head = node_list[num_list[0]]
    pre_node = head
    for i in xrange(1, len(num_list)):
        node = node_list[num_list[i]]
        pre_node.next = node
        pre_node = node
    return head


# 
# Method1. Need to get the length of two two linked lists.
# The main idea:
# linked list A: l1 = a1 + b
# linked list B: l2 = a2 + b
# The intersected node is at the position that before "b", and l2 - l1 = a2 -
# a1. We can firstly go abs(l2 - l1) steps from the head of the longer linked
# list, then go from the two heads step by step at the same time till arriving
# at the intersected node.
#
# Run time on LeetCode: 399 ms, beat 82.08%
#
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        lenA = 0
        while nodeA:
            nodeA = nodeA.next
            lenA += 1
        nodeB = headB
        lenB = 0
        while nodeB:
            nodeB = nodeB.next
            lenB += 1

        nodeA = headA
        nodeB = headB
        if lenA > lenB:
            for _ in xrange(lenA - lenB):
                nodeA = nodeA.next
        else:
            for _ in xrange(lenB - lenA):
                nodeB = nodeB.next

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None

# 
# Method2. Do not need to get the length of two two linked lists. But also need
# to traverse each linked list twice.
#
# Run time on LeetCode: 419 ms, beat 64.26%
#
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = headB if nodeA == None else nodeA.next
            nodeB = headA if nodeB == None else nodeB.next
        return nodeA

        
if __name__ == "__main__":
    test_cases = [
        (None, None),
        (None, [1,2]),
        ([1], None),
        ([1], [2,3]),
        ([1,2,3,4], [3,4]),
        ([1,2,3,4], [5,6,3,4]),
        ([1,2,3,4], [5,6,7,3,4]),
        ([1,2,3,4], [1,2,3,4]),
    ]
    solu = Solution()
    for num_array1, num_array2 in test_cases:
        node_array = []
        for i in xrange(10):
            node_array.append(ListNode(i))
        head1 = constructLinkWithUniqVals(num_array1, node_array)
        head2 = constructLinkWithUniqVals(num_array2, node_array)
        printLink(head1)
        printLink(head2)
        res = solu.getIntersectionNode(head1, head2)
        print res.val if res else None

        print "\n"
