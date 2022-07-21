#!/usr/bin/python3
""" Create a singly linked list"""


class Node:
    """defines a node of a singly linked list

    Attributes:
        data (int): data of note
        next_node (Node): must be None, the next node of this
    """

    def __init__(self, data, next_node=None):
        """Init the class object by new data

        Args:
            data (int): data of note
            next_node (Node or None): the next node of this
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data: property

        Returns:
            data of node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data: set data of node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node:  property

        Returns:
            next_node of node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node: set next_node of node"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance
        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """Represents a single linked list

    Attributes:
        __head (Node): head of the linked list
    """

    def __init__(self):
        """Initializes the linked list

        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node instance into the correct sorted position
        Args:
            value (int): data stored inside the new node

        Returns:
            None
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            if (self.__head.data > value):
                new_node.next_node, self.__head = self.__head, new_node
            else:
                my_node = self.__head
                while type(my_node.next_node) is Node:
                    if value < my_node.next_node.data:
                        break
                    my_node = my_node.next_node

                new_node.next_node = my_node.next_node
                my_node.next_node = new_node

    def __str__(self):
        """String representation of SinglyLinkedList instance
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
