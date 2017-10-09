__author__ = "akhtar"


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_front(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node

	def insert_in_between(self, data, position):
		node = Node(data)
		temp = self.head

		if self.head is None:
			print("List is empty, inserting as first element.")
			self.head = node
			return

		if position == 1:
			node.next = self.head
			self.head = node
			return

		if position == 0:
			print("Cannot insert at this position.")
			return

		for i in range(1, position - 1):
			temp = temp.next
			if temp is None:
				print("Cannot insert at this position.")
				return

		node.next = temp.next
		temp.next = node

	def insert_at_end(self, data):
		node = Node(data)

		if self.head is None:
			self.head = node
			return

		temp = self.head
		while (temp.next):
			temp = temp.next

		temp.next = node

	def delete_node(self, data):
		temp = self.head
		previous = self.head

		if self.head is None:
			print("List is empty.")
			return

		if self.head.data == data:
			self.head = self.head.next
			return

		while temp.data != data:
			previous = temp
			temp = temp.next
			if temp is None:
				print("Data not found in the list.")
				return

		previous.next = temp.next

	def delete_node_at_position(self, position):
		temp = self.head

		if self.head is None:
			print("List is empty.")
			return

		if position == 0:
			print("Cannot delete at this position.")
			return

		if position == 1:
			self.head = self.head.next
			return

		for i in range(1, position - 1):
			temp = temp.next
			if temp is None:
				print("Cannot delete at this position.")
				return

		if temp.next is None:
			print("Cannot delete at this position.")
			return

		temp.next = temp.next.next

	def length_iterative(self):
		length = 0

		if self.head is not None:
			temp = self.head
			while temp:
				length += 1
				temp = temp.next

		return length

	def length_recursive(self):
		def get_length(node):
			if not node:  # Base case
				return 0
			else:
				return 1 + get_length(node.next)

		return get_length(self.head)

	# TODO: Swap 2 nodes of a list.
	def swap_nodes(self, first_data, second_data):
		pass

	def reverse(self):
		previous = None
		current = self.head

		while current is not None:
			next = current.next
			current.next = previous
			previous = current
			current = next

		self.head = previous

	def reverse_in_groups(self, head, k):

		# Recursive solution
		current = head
		next = None
		previous = None
		first = head
		count = 0

		while current is not None and count < k:
			next = current.next
			current.next = previous
			previous = current
			current = next
			count += 1

		if head == self.head:
			self.head = previous

		if next is not None:
			first.next = self.reverse_in_groups(next, k)

		return previous

		######## Iterative solution ########
		# curr = head
		# previous = None
		# last = None
		# while curr:
		# 	count = 0
		# 	current = curr
		# 	first = curr
		# 	while current and count < k:
		# 		next = current.next
		# 		current.next = previous
		# 		previous = current
		# 		current = next
		# 		count += 1
		#
		# 	if last:
		# 		last.next = previous
		# 	last = first
		# 	curr = current
		# 	if self.head == head:
		# 		self.head = previous
		# 	previous = first
		#
		# if previous:
		# 	previous.next = None

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ", flush=True)
			temp = temp.next
		print()
