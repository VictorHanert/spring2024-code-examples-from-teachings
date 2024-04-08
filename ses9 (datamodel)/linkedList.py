class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.__dict__}'

class LinkedList:
     def __init__(self):
          self.head = None
    
     def __repr__(self):
        return f'{self.__dict__}'
    
llist = LinkedList()
llist.head = Node('Data of first Node')
llist.head.next = Node('Data of second Node')