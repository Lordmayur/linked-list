class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def iterate_items(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

ll = LinkedList()
ll.insert("welcome to")
ll.insert("HKE Polytechnic")
ll.insert("DS lab")
ll.insert("4th semester")

print("List:")
for val in ll.iterate_items():
    print(val)