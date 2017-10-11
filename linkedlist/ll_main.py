from linkedlist.linkedlist import LinkedList, Node

__author__ = "akhtar"

# Create the linked list
llist = LinkedList()
llist.create_list(head=Node(1), second=Node(35), third=Node(3), fourth=Node(11), fifth=Node(2), sixth=Node(99))

print("\nInitial list:", end=" ")
llist.print_list()
print("Length of linked list (iterative): {0}".format(llist.length_iterative()), end="\n\n")
print("Length of linked list (recursive): {0}".format(llist.length_recursive()), end="\n\n")

llist.insert_at_front(5)
print("After inserting 5 at beginning:", end=" ")
llist.print_list()

llist.insert_at_end(9)
print("After inserting 9 at end:", end=" ")
llist.print_list()

llist.insert_in_between(61, 2)
print("After inserting 61 at second position:", end=" ")
llist.print_list()

llist.delete_node(2)
print("After deleting 2:", end=" ")
llist.print_list()

llist.delete_node_at_position(4)
print("After deleting element at 4th position:", end=" ")
llist.print_list()

llist.reverse()
print("After reversing the list:", end=" ")
llist.print_list()

llist.reverse_in_groups_recursive(llist.head, 3)
print("After reversing in groups of 3 (recursive solution):", end=" ")
llist.print_list()

llist.reverse_in_groups_iterative(llist.head, 2)
print("After reversing in groups of 2 (iterative solution):", end=" ")
llist.print_list()

# Create the looped linked list
loop_list = LinkedList()
loop_list.create_list(head=Node(1), second=Node(35), third=Node(3), fourth=Node(11), fifth=Node(2), sixth=Node(99), loop=True)
print(loop_list.find_loop_and_remove(), end=" ")
loop_list.print_list()
