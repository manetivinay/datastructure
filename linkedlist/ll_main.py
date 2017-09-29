from linkedlist.linkedlist import LinkedList, Node

__author__ = "akhtar"


llist = LinkedList()  # Start with the empty list

# Create 3 nodes
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second  # Link first node with second
second.next = third  # Link second node with the third node

llist.print_list()
