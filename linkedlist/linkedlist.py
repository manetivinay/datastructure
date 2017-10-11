__author__ = "akhtar"


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def create_list(self, **kwargs):
		self.head = kwargs.get("head")
		second = kwargs.get("second")
		third = kwargs.get("third")
		fourth = kwargs.get("fourth")
		fifth = kwargs.get("fifth")
		sixth = kwargs.get("sixth")

		self.head.next = second  # Link first node with second one
		second.next = third  # Link second node with the third one
		third.next = fourth  # Link third node with the fourth one
		fourth.next = fifth  # Link fourth node with the fifth one
		fifth.next = sixth  # Link fifth node with the sixth one

		loop = kwargs.get("loop")
		if loop:
			sixth.next = third

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

	def reverse_in_groups_recursive(self, head, k):
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
			first.next = self.reverse_in_groups_recursive(next, k)

		return previous

	def reverse_in_groups_iterative(self, head, k):
		curr = head
		previous = None
		last = None
		while curr:
			count = 0
			current = curr
			first = curr
			while current and count < k:
				next = current.next
				current.next = previous
				previous = current
				current = next
				count += 1

			if last:
				last.next = previous
			last = first
			curr = current
			if self.head == head:
				self.head = previous
			previous = first

		if previous:
			previous.next = None

	def find_loop_and_remove(self):
		hare = self.head
		tortoise = self.head
		loop_exists = False

		while hare is not None and hare.next is not None:
			hare = hare.next.next
			tortoise = tortoise.next

			if hare == tortoise:
				loop_exists = True
				break

		if loop_exists:
			tortoise = self.head

			prev = None
			while tortoise != hare:
				prev = hare
				tortoise = tortoise.next
				hare = hare.next

			prev.next = None

			return "Loop exists, loop start point = {0}, List after removing loop: ".format(hare.data)

		return "No loop exists. List:"

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ", flush=True)
			temp = temp.next
		print("\n")
