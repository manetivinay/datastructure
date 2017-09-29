__author__ = "akhtar"


# Node class
class Node:
	# Function to initialize the node object
	def __init__(self, data):
		self.data = data  # Assign data
		self.next = None  # Initialize next as null


# Linked List class
class LinkedList:
	# Function to initialize the LinkedList object
	def __init__(self):
		self.head = None

	# This function prints contents of linked list starting from head
	def print_list(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next
