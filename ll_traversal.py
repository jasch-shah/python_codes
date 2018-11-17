from __future__ import print_function

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.Head = None	# initialize Head to None

	def insert_tail(self, data):
		if(self.Head is None): self.insert_head(data)
		else:
			temp = self.Head
			while(temp.next != None):
				temp = temp.next
			temp.next = Node(data)
	

	def insert_head(self, data):
		newNod = Node(data)
		if self.Head != None:
			newNod.next = newNod
		self.Head = newNod
	

	def printList(self):
		temp = self.Head
		while temp is not None:
			print(temp.data)
			temp = temp.next

	def delete_head(self):
		temp = self.Head
		if self.Head != None:
			self.Head = self.Head.next
			temp.next = None
		return temp
	

	def delete_tail(self):
		temp = self.Head
		if self.Head != None:
			if(self.Head.next is None):
				self.Head = None
			else:
				while temp.next.next is not None:
					temp = temp.next
				temp.next, temp = None, temp.next
		return temp

	
	def isEmpty(self):
		return self.Head is None 

	def reverse(self):
		prev = None
		current = self.Head

		while current:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node
		self.Head = prev
	

def main():
	A = LinkedList()
	print("Inserting 10 as head")
	A.insert_head(10)
	print("Inserting 0 as head")
	A.insert_head(0)
	print("\nPrint list")
	A.printList()
	print("\nInserting 100 as tail")
	A.insert_tail(100)
	print("\n Inserting 1000 as tail")
	A.insert_tail(1000)
	print("\nPrint List")
	A.printList()
	print("\nDelete Head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.printList()
    print("\nReverse Linked List")
    A.reverse()
    print("\nPrint List : ")
    A.printList()


	
if __name__ == '__main__':
	main()	
