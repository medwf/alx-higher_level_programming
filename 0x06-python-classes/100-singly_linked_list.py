#!/usr/bin/python3
"""This is class SinglyLinkedList"""


class Node:
    """  This class allows you to create and manipulate SinglyLinkedList objects """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @data.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(int(node.data))
            node = node.next_node
        return "\n".join(nodes)
