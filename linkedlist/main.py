# from linkedlist.linkedlist import LinkedList, Node
from linkedlist import linkedlist as ll

__author__ = "akhtar"

# A simple Python program to introduce a linked list

# if __name__ == '__main__':

# Start with the empty list
llist = ll.LinkedList()

# Create 3 nodes
llist.head = ll.Node(1)
second = ll.Node(2)
third = ll.Node(3)

llist.head.next = second  # Link first node with second
second.next = third  # Link second node with the third node

llist.print_list()
