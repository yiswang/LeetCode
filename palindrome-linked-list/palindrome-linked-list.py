#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        palindrome-linked-list.py
# Create Date: 2017-02-23
# Usage:       palindrome-linked-list.py
# Description:
#
# LeetCode problem 234. Palindrome Linked List Add to List
#
# Difficulty: Easy
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
###############################################################################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#
# Method 1. Need to get the link length.
# Run time on LeetCode: 179ms, beat 27.38%; 312ms, beat 2.99%; 165ms, beat 44.39%
#
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        length = 0
        currNode = head
        while currNode:
            length += 1
            currNode = currNode.next

        semiLength = length / 2
        currNode = head
        for _ in xrange(semiLength):
            currNode = currNode.next

        prevNode = currNode
        currNode = currNode.next
        reverseCount = 0
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            reverseCount += 1

        lastNode = prevNode
        node1 = head
        node2 = lastNode
        flag = True
        for _ in xrange(semiLength):
            if node1.val != node2.val:
                flag = False
                break
            node1, node2 = node1.next, node2.next

        prevNode = None
        currNode = lastNode
        for _ in xrange(reverseCount):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        return flag


#
# Method 2. Do not need to get the link length.
# Run time on LeetCode: 152, beat 65.14%
#
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        flag = True
        while rev:
            flag = flag and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return flag


if __name__ == "__main__":
    pass
