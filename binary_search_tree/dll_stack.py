from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.len() == 0:
            return None
        else:
            return self.storage.remove_from_head()

    def len(self):
        if self.size == 0:
            return 0
        else:
            return self.storage.__len__()
