# write a Node construct and a linkedlist construct
#write a Pop first method

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail =new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        #check if list empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail =new_node
        
        self.length +=1
    
    def pop_first(self,value):
        #check empty list
        if self.head ==None:
            return None
        
        #move the head to the next node
        temp = self.head
        self.head = self.head.next
        self.length -=1
        if self.length == 0:
            #empty out the list
            self.tail = None
        temp.next = None
        return temp
    