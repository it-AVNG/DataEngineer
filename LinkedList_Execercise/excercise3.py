#write a node and linked list constructor
#write a pop method, to remove and return the las vaue from the list

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

    def pop(self,value):
        #check empty list
        if self.head.next == None :
            return None 
        
        #find the last value
        #by create a pointer pair set them at the start
        temp =self.head
        pre=self.head
        #and iterate through the list
        while (temp.next):
            pre = temp
            temp =temp.next 

        #Move the tail to the 2nd-to-last value
        self.tail = pre
        
        #point the next value to None and return the last value
        self.tail.next= None
        self.length -=1
        
        #if pop would empty the list
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp