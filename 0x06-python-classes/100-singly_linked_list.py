#!/usr/bin/python3
"""This is class Node"""


class Node:
    """  This class allows you to create and manipulate Node objects """

    def __init__(self, data, next_node=None):
        """ Initialize a new Square
        Args:
            data (int): data for node
            next_node(Node): pointer to None or Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of Node

        Returns:
            int: The data of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set The data of the Node.

        Args:
            value (int): The integer of the node.

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieve the next_node of The Node

        Returns:
            next_node: None or next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set The next_node of the Node.

        Args:
            value (Node): The next Node or None.

        Raises:
            TypeError: next_node must be a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


"""This is class SinglyLinkedList"""


class SinglyLinkedList:
    """  This class allows you to create and manipulate SinglyLinkedList objects """

    def __init__(self):
        """ Initialize a new SinglyLinkedList """
        self.head = None

    def sorted_insert(self, value):
        """Methode to sorted insert value """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __repr__(self):
        """  method that prints the entire list in stdout, one node number by line. """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)
