class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        #create a node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # def append(self,value):
    #     #create a node
    #     new_node = Node(value)
    #     #add Node to end
    # def prepend(self,value):
    #     #create a node
    #     new_node = Node(value)
    #     #add Node to the beginning
    # def insert(self,value):
    #     #create a node
    #     new_node = Node(value)
    #     #insert the node to desired place

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)