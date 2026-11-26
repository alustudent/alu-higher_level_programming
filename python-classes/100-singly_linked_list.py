#!/usr/bin/python3
"""Defines a Node and a sorted SinglyLinkedList."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node with validated data and next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data, which must be an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node, which must be None or a Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list kept in increasing order."""

    def __init__(self):
        """Initializes an empty list."""
        self.__head = None

    def __str__(self):
        """Returns the node values, one per line."""
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node at its sorted position."""
        new = Node(value)
        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        node = self.__head
        while node.next_node is not None and node.next_node.data < value:
            node = node.next_node
        new.next_node = node.next_node
        node.next_node = new
