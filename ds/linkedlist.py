# implementing linkedinlist in python


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
# node can be single only too so next_node is None . it can change later as elements are added to ll

class Linkedlist:
    def __init__(self):
        self.head = None
        # initially the head is emtpy

    def append(self, data):
        # append means adding new node to the ll so we need to create a new node with data using Node class
        new_node = Node(data)
          
