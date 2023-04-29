#Write aNode and a LinkedList Construct
#Write prependmethod

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail =new_node
        self.length =1
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head =new_node
            self.tail =new_node
        else:
          self.tail.next = new_node
          self.tail = new_node
        self.length +=1
    
    def prepend(self,value):
        #create a node
        new_node = Node(value)
        #check if list empty
        if self.head == None:
            self.head =new_node
            self.tail =new_node
        else:
            #point the new node to the current head
            new_node.next = self.head
            
            #move the head to the new node
            self.head = new_node
        
        self.length+=1
        return True
