#write a node and linked list constructor
#Add append method to the linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node =Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):
        new_node =Node(value)
        # if the list is not created or empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
          # If there is a tail element from the list
          #point the tail node to the new node
          self.tail.next = new_node
          #move the tail to the new node
          self.tail =new_node
        #increase the length of the linked list
        self.length += 1
    
    
        

