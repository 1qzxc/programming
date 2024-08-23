# written by https://github.com/mikefrostov
# 
# Aim: show the implementation of the signly linked list
# 
# Linked list is a data structure that has a number of nodes that are 
# linked to each other only once like this: 
#
# {NODE1[payload][pointer_to_next_node]} -> {NODE2[payload][pointer_to_next_node]}
#
# pre-pend operation takes O(1)
#
# append takes O(n) since we have to traverse the list in order to append new node 
#
# NODE object consists of a "payload" and a "pointer to next node" 
#
# Linked List consists of NODE objects, head, a counter, print method, append method, prepend method, init method
#
#


class MyList:

    def __init__(self, *values):
        self.head = None
        self.cursor = self.head
        for value in values:
            node = Node(value)
            if self.head is None:
                self.head = node
            else:
                self.append_node(node)
        self.cursor = self.head    # cursor needs to always start from the head

    @property
    def _value(self):
        return self.head._value

    @_value.setter
    def _value(self, val):
        self.head._value = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor is None:
            self.cursor = self.head
            raise StopIteration
        value = self.cursor._value
        self.cursor = self.cursor._pointer
        return value

    def __add__(self, operand):
        if isinstance(operand, Node):
            self.append_node(operand)
        if isinstance(operand, int):
            self.append(operand)
        if isinstance(operand, MyList):
            for value in operand:
                self.append(value)
            return self
        if isinstance(operand, list):
            for value in operand:
                self.append(int(value))
        if isinstance(operand, tuple):
            for value in operand:
                self.append(int(value))
        return self

    def prepend_node(self, node):
        node._pointer = self.head
        self.head = node

    def append_node(self, new_node):
        if self.head is None:
            self.head = new_node
            return self
        self.cursor = self.head
        while self.cursor._pointer is not None:
            self.cursor = self.cursor._pointer
        self.cursor._pointer = new_node
        self.cursor = self.head
        return self

    def append(self, value):
        node = Node(value)
        self.append_node(node)
        return self

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def reverse(self):
        pass

    def print(self):
        self.cursor = self.head
        temp = ''
        while self.cursor is not None:
            temp = temp + ' ' + str(self.cursor._value)
            self.cursor = self.cursor._pointer
        print(temp)
        self.cursor = self.head

    def print_reversed(self):  # using reversed string
        self.cursor = self.head
        temp = ''
        while self.cursor is not None:
            temp = temp + " " + str(self.cursor._value)
            self.cursor = self.cursor._pointer
        temp1 = ''
        for c in temp:
            temp1 = c + temp1  # appending chars in reverse order
        print(temp1)
        self.cursor = self.head

class Node:

    def __init__(self, _value, _pointer=None):
        self._value = _value
        self._pointer = _pointer
