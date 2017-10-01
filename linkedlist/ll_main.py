from linkedlist.linkedlist import LinkedList, Node

__author__ = "akhtar"


llist = LinkedList()  # Start with the empty list

# Create 3 nodes
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second  # Link first node with second one
second.next = third  # Link second node with the third one

llist.insert_at_front(5)
llist.insert_at_end(9)
llist.insert_in_between(61, 2)

llist.print_list()
