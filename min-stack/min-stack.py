#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        min-stack.py
# Create Date: 2017-02-08
# Usage:       min-stack.py
# Description:
#
# LeetCode problem 155. Min Stack
#
# Difficulty: Easy
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
###############################################################################


#
# Use two buffers, one stores the stack elements, and the other one stores the
# current minimum elements at each top of the stack.
# Run time on LeetCode: 122ms, beat 30.25%; 106ms, 41.34%
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__CAPACITY = 2
        self.__buffer = [None] * self.__CAPACITY
        self.__minValBuffer = [None] * self.__CAPACITY
        self.__top = -1
        self.__minVal = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.__top + 2 == self.__CAPACITY:
            self.__buffer += [None] * self.__CAPACITY
            self.__minValBuffer += [None] * self.__CAPACITY
            self.__CAPACITY *= 2
        self.__top += 1
        self.__buffer[self.__top] = x
        if (self.__minVal == None) or (x < self.__minVal):
            self.__minVal = x
        self.__minValBuffer[self.__top] = self.__minVal
        

    def pop(self):
        """
        :rtype: void
        """
        if self.__top >= 0:
            self.__top -= 1
            self.__minVal = self.__minValBuffer[self.__top]
        

    def top(self):
        """
        :rtype: int
        """
        if self.__top >= 0:
            return self.__buffer[self.__top]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.__minVal
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

        
if __name__ == "__main__":
    obj = MinStack()

    obj.push(3)
    print obj.top()
    print obj.getMin()
    print ""

    obj.push(0)
    print obj.top()
    print obj.getMin()
    print ""

    obj.push(1)
    print obj.top()
    print obj.getMin()
    print ""

    obj.pop()
    print obj.top()
    print obj.getMin()
    print ""

    obj.pop()
    print obj.top()
    print obj.getMin()
    print ""

    obj.pop()
    print obj.top()
    print obj.getMin()
    print ""

    obj.pop()
    print obj.top()
    print obj.getMin()
    print ""
